import sqlite3

class Fornecedor:
    def __init__(self, nome, cnpj, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone

    def salvar_no_banco(self):
        # Conectar ao banco de dados SQLite (ou criar se não existir)
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Criar a tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fornecedores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cnpj TEXT,
                telefone TEXT
            )
        ''')


        # Inserir o fornecedor na tabela
        cursor.execute('''
            INSERT INTO fornecedores (nome, cnpj, telefone)
            VALUES (?, ?, ?)
        ''', (self.nome, self.cnpj, self.telefone))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def novo_fornecedor(nome,cnpj,telefone):
        fornecedor = Fornecedor(nome, cnpj, telefone)
        fornecedor.salvar_no_banco()

    @staticmethod
    def atualizar_fornecedor(id, nome, cnpj, telefone):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Atualizar o fornecedor na tabela
        cursor.execute('''
            UPDATE fornecedores
            SET nome = ?, cnpj = ?, telefone = ?
            WHERE id = ?
        ''', (nome, cnpj, telefone, id))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_fornecedor(id):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Excluir o fornecedor na tabela
        cursor.execute('DELETE FROM fornecedores WHERE id = ?', (id,))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_fornecedores():
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar todos os fornecedores na tabela
        cursor.execute('SELECT * FROM fornecedores')
        fornecedores = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return fornecedores