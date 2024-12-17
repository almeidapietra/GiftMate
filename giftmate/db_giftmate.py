import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('giftmate.db')
cursor = conn.cursor()

# Criando a tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL,
    categoria TEXT,
    faixa_etaria TEXT
)
''')

# Inserindo dados no banco
produtos = [
    ("Bola de Futebol", "Bola de futebol de couro sintético, ideal para jogos de rua.", 79.90, "Esportes", "Crianças"),
    ("Console Playstation 5", "Console de última geração, com gráficos 4K e novos jogos exclusivos.", 4999.00, "Eletrônicos", "Adolescentes"),
    ("Boneca de Pelúcia", "Boneca de pelúcia com roupas trocáveis. Perfeita para crianças pequenas.", 59.90, "Brinquedos", "Crianças"),
    ("Camiseta Estilo Geek", "Camiseta com estampas dos principais jogos e filmes de cultura pop.", 49.90, "Roupas", "Adolescentes"),
    ("Echo Dot", "Assistente virtual Alexa em miniatura. Perfeito para automação da casa.", 249.00, "Eletrônicos", "Adultos"),
    ("Livro: O Senhor dos Anéis", "A obra-prima de J.R.R. Tolkien. Uma viagem épica pela Terra-média.", 59.90, "Livros", "Jovens Adultos"),
    ("Kit de Jardinagem", "Kit completo para cultivo de plantas em casa, com vasos e sementes.", 99.90, "Decoração", "Adultos"),
    ("Fones de Ouvido Bluetooth", "Fones de ouvido sem fio, com ótima qualidade de som e conforto.", 299.00, "Eletrônicos", "Adultos"),
    ("Cesta de Café da Manhã", "Cesta com diversos itens de café da manhã, como pães, bolos e sucos.", 129.90, "Presentes", "Adultos"),
    ("Conjunto de Chá de Porcelana", "Conjunto de chá de porcelana com xícaras e pires, ideal para presentes sofisticados.", 199.90, "Presentes", "Adultos"),
    ("Caixa de Ferramentas", "Caixa de ferramentas completa para consertos e pequenas reformas.", 159.90, "Ferramentas", "Adultos"),
    ("Carrinho de Controle Remoto", "Carrinho de controle remoto, ótimo para crianças e adolescentes.", 199.00, "Brinquedos", "Crianças"),
    ("Fazendo Arte: Kit de Pintura", "Kit completo com tintas, pincéis e telas para iniciantes.", 79.90, "Arte", "Adolescentes"),
    ("Tênis de Corrida", "Tênis confortável e adequado para corridas e atividades físicas.", 249.00, "Roupas", "Adultos"),
    ("Câmera Fotográfica", "Câmera fotográfica de alta definição para iniciantes e profissionais.", 1599.00, "Eletrônicos", "Adultos"),
]

# Inserindo os produtos na tabela
cursor.executemany('''
INSERT INTO produtos (nome, descricao, preco, categoria, faixa_etaria)
VALUES (?, ?, ?, ?, ?)
''', produtos)

# Confirmando as inserções
conn.commit()
conn.close()

print("Banco de dados de produtos criado e populado com sucesso!")