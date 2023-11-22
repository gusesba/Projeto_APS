import sqlite3

class Usuario:
    def __init__(self,usuario,senha,cargo):
        self.usuario = usuario
        self.senha = senha
        self.cargo = cargo

    @staticmethod
    def novo_usuario(usuario,senha, cargo):
        usuario = Usuario(usuario,senha,cargo)
        usuario.salvar_no_banco()

    @staticmethod
    def autenticar(usuario, senha):
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar o usuário com o nome de usuário e senha informados
        cursor.execute('SELECT * FROM usuarios WHERE usuario = ? AND senha = ?', (usuario, senha))
        usuario = cursor.fetchone()

        # Fechar a conexão
        conexao.close()

        # Retornar o usuário encontrado
        return usuario

    def salvar_no_banco(self):
        # Conectar ao banco de dados SQLite (ou criar se não existir)
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Criar a tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT,
                senha TEXT,
                cargo TEXT
            )
        ''')

        # Inserir o usuário na tabela
        cursor.execute('''
            INSERT INTO usuarios (usuario, senha, cargo)
            VALUES (?, ?, ?)
        ''', (self.usuario, self.senha, self.cargo))

        # Commit e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_usuarios():
        # Conectar ao banco de dados SQLite
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()

        # Selecionar todos os usuários na tabela
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()

        # Fechar a conexão
        conexao.close()

        return usuarios