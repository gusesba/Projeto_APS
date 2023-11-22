import sqlite3

class Cliente:
    def __init__(self, nome, cnpj, cpf, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.cpf = cpf
        self.telefone = telefone

    def salvar_no_banco(self):
        # Conectar ao banco de dados SQLite (ou criar se não existir)
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Criar a tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cnpj TEXT,
                cpf TEXT,
                telefone TEXT
            )
        ''')

        # Inserir o cliente na tabela
        cursor.execute('''
            INSERT INTO clientes (nome, cnpj, cpf, telefone)
            VALUES (?, ?, ?, ?)
        ''', (self.nome, self.cnpj, self.cpf, self.telefone))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def novo_cliente(nome, cnpj, cpf, telefone):
        cliente = Cliente(nome, cnpj, cpf, telefone)
        cliente.salvar_no_banco()

    @staticmethod
    def excluir_cliente(id):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Excluir o cliente na tabela
        cursor.execute('''
            DELETE FROM clientes
            WHERE id = ?
        ''', (id,))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def atualizar_cliente(id, nome, cnpj, cpf, telefone):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Atualizar o cliente na tabela
        cursor.execute('''
            UPDATE clientes
            SET nome = ?, cnpj = ?, cpf = ?, telefone = ?
            WHERE id = ?
        ''', (nome, cnpj, cpf, telefone, id))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_clientes():
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar todos os clientes na tabela
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return clientes