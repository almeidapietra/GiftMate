# **GiftMate - Assistente Virtual de Presentes**

## **Descrição do Projeto**

**GiftMate** é um assistente virtual projetado para facilitar a escolha de presentes, especialmente em situações como datas comemorativas, aniversários e outras ocasiões especiais. O projeto foi criado com base em uma necessidade pessoal ao tentar escolher presentes adequados para amigos e familiares. Durante essas experiências, percebi a dificuldade de encontrar algo que realmente combinasse com a pessoa, levando em consideração fatores como idade, gosto e interesses. O GiftMate surgiu como uma solução para esse problema, ajudando usuários a fazerem escolhas mais acertadas ao presentearem outros.

Este MVP (Mínimo Produto Viável) foi desenvolvido para demonstrar o conceito, utilizando dados simulados em um banco de dados SQLite. No futuro, poderia ser integrado a dados de produtos reais de sites de vendas, criando uma experiência dinâmica e personalizada para os usuários.

## **Como Funciona**

O GiftMate oferece uma interação simples e direta com o usuário, onde você pode fornecer características da pessoa que deseja presentear (como idade, interesses e preferências) e o assistente sugere os melhores produtos com base nessas informações.

Apesar de, neste momento, o banco de dados ser simulado, o sistema está estruturado para se integrar facilmente a bancos de dados reais, como os de sites de e-commerce, permitindo uma dinâmica mais robusta e realista.

## **Tecnologias Utilizadas**

- **Python**: Linguagem principal do projeto, usada para lógica de negócio e integração com outras ferramentas.
- **SQLite**: Banco de dados utilizado para simular a base de dados de produtos e usuários. Ele armazena as informações de produtos e sugestões, facilitando a consulta e manipulação.
- **Langchain**: Framework que facilita a criação de pipelines de processamento de linguagem natural (NLP). Utilizado para a interação com o modelo de IA e para gerar respostas inteligentes e personalizadas para os usuários.
- **Amazon Bedrock**: Serviço da AWS que oferece acesso a poderosas modelos de inteligência artificial, como o **Claude-v2** da Anthropic. Utilizei o Bedrock para fornecer as respostas da IA, fazendo com que o GiftMate seja mais inteligente e capaz de oferecer sugestões realmente úteis.
- **API do LangChain**: Usei o LangChain para treinar a IA com prompts generativos e adaptá-la até que ela fosse capaz de fornecer respostas precisas e claras, alinhadas às minhas expectativas.

## **Amazon Bedrock**

O **Amazon Bedrock** é um serviço da AWS que fornece acesso a modelos de IA poderosos, incluindo modelos como o **Claude-v2** da Anthropic. Ele oferece a capacidade de integrar esses modelos em diversas aplicações e é projetado para escalabilidade e flexibilidade. O uso do Amazon Bedrock em GiftMate possibilitou uma IA eficiente e com capacidade de personalizar respostas de acordo com as características dos produtos e preferências do usuário. Ao integrar essa solução, foi possível criar um assistente que simula a interação humana com alta qualidade e de forma muito intuitiva.

## **Modelo de IA Utilizado**

Utilizei o modelo **Claude-v2** da Anthropic, integrado por meio do **Amazon Bedrock**. Este modelo é especializado em responder de maneira natural e contextualizada a perguntas sobre uma ampla gama de tópicos, incluindo recomendações de produtos. O modelo foi treinado usando **prompt engineering**, uma técnica que permite ajustar os parâmetros de entrada para que a IA forneça respostas mais precisas e personalizadas. Ao longo do desenvolvimento, fui ajustando o treinamento até que a IA pudesse responder de forma eficiente e fluida, como você pode ver nas interações do GiftMate.

## **Objetivo e Expansão do Projeto**

O objetivo principal do GiftMate é ajudar as pessoas a escolherem presentes de maneira mais inteligente, levando em consideração dados relevantes como a idade, preferências e interesses do presenteado. Em vez de navegar por centenas de páginas de produtos sem saber ao certo o que escolher, o GiftMate utiliza IA para recomendar as melhores opções com base em dados reais e específicos.

### **Expansão Possível**
- **Integração com E-commerce**: O projeto foi desenvolvido com a possibilidade de integração com bancos de dados de produtos de plataformas de e-commerce. Isso permitiria ao GiftMate acessar e recomendar produtos reais de diversas lojas online.
- **Personalização Dinâmica**: À medida que o GiftMate vai aprendendo mais sobre os usuários e suas preferências, ele se torna cada vez mais assertivo nas sugestões de presentes.
- **Interface de Usuário**: Embora o MVP seja um protótipo de linha de comando, uma versão futura poderia ser desenvolvida com uma interface web ou aplicativo, melhorando ainda mais a experiência do usuário.

## **Como Integrar GiftMate com Sua Empresa**

O GiftMate não é apenas uma ferramenta divertida para escolher presentes. Ele pode ser integrado aos dados de produtos de sua empresa ou de plataformas de e-commerce, oferecendo uma experiência personalizada para seus clientes.

- **Recomendações Personalizadas**: Ao integrar GiftMate com a base de dados de produtos da sua empresa, ele pode sugerir presentes com base nas preferências dos clientes, aumentando a taxa de conversão e satisfação do usuário.
- **Análise de Dados**: A IA pode analisar as interações dos clientes com o assistente, ajudando sua empresa a entender melhor as preferências de compra e oferecendo insights para melhorar o portfólio de produtos.
- **Escalabilidade na Nuvem**: Com o uso do Amazon Bedrock, o GiftMate pode ser escalado para suportar grandes volumes de usuários e dados, sem comprometer a performance.

## **Conclusão**

GiftMate é uma solução inovadora que usa inteligência artificial para ajudar as pessoas a escolherem presentes com mais assertividade e eficiência. Este MVP foi criado como um protótipo, mas tem o potencial de ser expandido para uma plataforma robusta, que pode ser integrada com lojas online, empresas de e-commerce, ou qualquer outro serviço que deseje melhorar a experiência do cliente na escolha de produtos.

Se você está buscando uma forma de personalizar a experiência de compra de seus clientes ou deseja proporcionar uma ferramenta de recomendação inteligente, o GiftMate é uma excelente solução, baseada em IA e pronta para ser adaptada à sua plataforma.

## **Como Rodar o Projeto**

1. Clone este repositório:  
   ```bash
   git clone https://github.com/almeidapietra/GiftMate
   ```

2. Instale as dependências:
    ```bash
   pip install -r requirements.txt
   ```

3. Execute o script principal:
    ```bash
   python giftmate.py
   ```

4.  Interaja com o assistente de presentes e aproveite as sugestões inteligentes! 

## meus contatos:
<div> 
    <a href = "mailto:costapietra@gmail.com"><img loading="lazy" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="https://www.linkedin.com/in/almeidapietra" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
</div>