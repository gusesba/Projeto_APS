import sqlite3

class Entrada:
    def __init__(self, data, quantidade, produto_id):
        self.data = data
        self.quantidade = quantidade
        self.produto_id = produto_id

    def salvar_no_banco(self):
        # Conectar ao banco de dados SQLite (ou criar se não existir)
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entradas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE,
                quantidade INTEGER,
                produto_id INTEGER,
                FOREIGN KEY (produto_id) REFERENCES produtos (id),
            )
        ''')


        # Inserir a entrada na tabela
        cursor.execute('''
            INSERT INTO entradas (data, quantidade, produto_id)
            VALUES (?, ?, ?)
        ''', (self.data, self.quantidade, self.produto_id))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def nova_entrada(data, quantidade, produto_id):
        entrada = Entrada(data, quantidade, produto_id)
        entrada.salvar_no_banco()

    @staticmethod
    def listar_entradas():
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar todas as entradas na tabela
        cursor.execute('''
            SELECT entradas.id, data, quantidade, produtos.descricao
            FROM entradas
            LEFT JOIN produtos ON entradas.produto_id = produtos.id
        ''')
        entradas = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return entradas
