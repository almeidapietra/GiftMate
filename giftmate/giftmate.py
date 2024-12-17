import sqlite3
import boto3
from langchain_aws import BedrockLLM
from langchain_core.prompts import ChatPromptTemplate

# Configuração do banco de dados
conn = sqlite3.connect('giftmate.db')
cursor = conn.cursor()

# Configuração do cliente AWS Bedrock
bedrock_client = boto3.client(service_name='bedrock-runtime', region_name='us-west-2')

def configurar_modelo(client, max_tokens=200, temperature=0.5, top_p=0.9):
    return BedrockLLM(
        model_id='anthropic.claude-v2', 
        client=client
    )

modelo = configurar_modelo(bedrock_client)

historico = []

def get_hist():
    return "\n".join(historico)

# Função para consultar o banco de dados e obter produtos
def consulta_produto(categoria=None, faixa_etaria=None):
    conn = sqlite3.connect('giftmate.db')
    cursor = conn.cursor()

    query = "SELECT nome, descricao, preco, categoria, faixa_etaria FROM produtos WHERE 1=1"
    
    params = []
    
    if categoria:
        query += " AND categoria LIKE ?"
        params.append(f"%{categoria}%")
        
    if faixa_etaria:
        query += " AND faixa_etaria LIKE ?"
        params.append(f"%{faixa_etaria}%")

    cursor.execute(query, params)
    
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# Função para criar o prompt do chatbot
def get_chat_prompt(entrada):
    template = ChatPromptTemplate.from_messages(
        [
            ("system", 
             "Você é o assistente virtual GiftMate, especializado em ajudar os usuários a encontrar presentes para diferentes faixas etárias e interesses. "
             "Quando o usuário me fornecer uma faixa etária ou categoria, vou sugerir produtos de acordo com essas informações."),
             
            ("human", entrada),
            
            ("assistant", 
             "Forneça sugestões personalizadas de presentes, considerando as preferências ou a faixa etária mencionada pelo usuário. "
             "Se não houver produtos relevantes, informe o usuário e sugira tentar outra busca.")
        ]
    )
    return template

# Função para interagir com o modelo e retornar a resposta
def inv_modelo(prompt):
    # Tentando buscar produtos relacionados à solicitação
    produtos_encontrados = consulta_produto(categoria="eletrônicos", faixa_etaria="adolescentes")
    
    if produtos_encontrados:
        produtos_info = "\n".join([f"Nome: {f[0]}, Descrição: {f[1]}, Preço: R${f[2]:.2f}" for f in produtos_encontrados])
        prompt = f"Produtos encontrados:\n{produtos_info}\n{prompt}"
    else:
        prompt = f"Nenhum produto encontrado.\n{prompt}"

    chain = get_chat_prompt(prompt).pipe(modelo)
    response = chain.invoke({"funcionalidade_name": prompt})  
    return response

# Exemplo de interação com o assistente
print(
    "Assistente: Olá! Eu sou o GiftMate, seu assistente virtual para escolher presentes. Como posso ajudar você a encontrar o presente perfeito?"
)

while True:
    entrada = input("User: ")
    historico.append(f"Human: {entrada}")
    if entrada.lower() == "sair":
        break
    response = inv_modelo(entrada)
    resposta_formatada = f"Assistente:\n{response}\n"
    historico.append(f"Assistant: {resposta_formatada}")
    print(resposta_formatada)