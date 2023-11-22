import sqlite3

class Produto:
    def __init__(self, tipo, valor, descricao, fornecedor_id):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.fornecedor_id = fornecedor_id

    def salvar_no_banco(self):
        # Conectar ao banco de dados SQLite (ou criar se não existir)
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT,
                valor REAL,
                descricao TEXT,
                fornecedor_id INTEGER,
                FOREIGN KEY (fornecedor_id) REFERENCES fornecedores (id)
            )
        ''')


        # Inserir o produto na tabela
        cursor.execute('''
            INSERT INTO produtos (tipo, valor, descricao, fornecedor_id)
            VALUES (?, ?, ?, ?)
        ''', (self.tipo, self.valor, self.descricao, self.fornecedor_id))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def novo_produto(tipo, valor, descricao, fornecedor_id):
        produto = Produto(tipo, valor, descricao, fornecedor_id)
        produto.salvar_no_banco()

    @staticmethod
    def atualizar_produto(id, tipo, valor, descricao, fornecedor_id):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Atualizar o produto na tabela
        cursor.execute('''
            UPDATE produtos
            SET tipo = ?, valor = ?, descricao = ?, fornecedor_id = ?
            WHERE id = ?
        ''', (tipo, valor, descricao, fornecedor_id, id))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_produto(id):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Excluir o produto na tabela
        cursor.execute('''
            DELETE FROM produtos
            WHERE id = ?
        ''', (id,))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def pesquisar_produto(pesquisa):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Pesquisar o produto na tabela
        cursor.execute('''
            SELECT produtos.id, tipo, valor, descricao, fornecedores.nome
            FROM produtos
            LEFT JOIN fornecedores ON produtos.fornecedor_id = fornecedores.id
            WHERE tipo LIKE ?
            OR descricao LIKE ?
        ''', (pesquisa, pesquisa))
        produtos = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return produtos

    @staticmethod
    def buscar_produto(id):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Buscar o produto na tabela
        cursor.execute('''
            SELECT produtos.id, tipo, valor, descricao, fornecedor_id
            FROM produtos
            WHERE id = ?
        ''', (id,))
        produto = cursor.fetchone()

        # Fechar a conexão
        conexao.close()

        return produto

    @staticmethod
    def listar_produtos():
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar todos os produtos na tabela
        cursor.execute('''
            SELECT produtos.id, tipo, valor, descricao, fornecedor_id
            FROM produtos
        ''')
        produtos = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return produtos
