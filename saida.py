import sqlite3

class Saida:
    def __init__(self, data, quantidade, produto_id, cliente_id):
        self.data = data
        self.quantidade = quantidade
        self.produto_id = produto_id
        self.cliente_id = cliente_id

    def salvar_no_banco(self):
        # Conectar ao banco de dados SQLite (ou criar se não existir)
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE,
                quantidade INTEGER,
                produto_id INTEGER,
                cliente_id INTEGER,
                FOREIGN KEY (produto_id) REFERENCES produtos (id),
                FOREIGN KEY (cliente_id) REFERENCES clientes (id)
            )
        ''')

        # Inserir a saída na tabela
        cursor.execute('''
            INSERT INTO saidas (data, quantidade, produto_id, cliente_id)
            VALUES (?, ?, ?, ?)
        ''', (self.data, self.quantidade, self.produto_id, self.cliente_id))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def nova_saida(data, quantidade, produto_id, cliente_id):
        saida = Saida(data, quantidade, produto_id, cliente_id)
        saida.salvar_no_banco()

    @staticmethod
    def excluir_saida(id):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Excluir a saída na tabela
        cursor.execute('''
            DELETE FROM saidas
            WHERE id = ?
        ''', (id,))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_saidas_mes_atual():
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar todas as saídas na tabela
        cursor.execute('''
            SELECT saidas.id, data, quantidade, produtos.descricao, clientes.nome
            FROM saidas
            LEFT JOIN produtos ON saidas.produto_id = produtos.id
            LEFT JOIN clientes ON saidas.cliente_id = clientes.id
            WHERE strftime('%m', data) = strftime('%m', 'now')
        ''')
        saidas = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return saidas

    @staticmethod
    def resumo_fornecedor(id):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar todas as saídas na tabela
        cursor.execute('''
            SELECT saidas.id, data, quantidade, produto_id, cliente_id
            FROM saidas
            LEFT JOIN produtos ON saidas.produto_id = produtos.id
            WHERE produtos.fornecedor_id = ?
        ''', (id,))
        saidas = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return saidas

    @staticmethod
    def listar_saidas():
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar todas as saídas na tabela
        cursor.execute('''
            SELECT saidas.id, data, quantidade, produto_id, cliente_id
            FROM saidas
        ''')
        saidas = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return saidas
    
    
