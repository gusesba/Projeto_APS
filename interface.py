import tkinter as tk
from tkinter import ttk
from usuario import Usuario
from fornecedor import Fornecedor
from produto import Produto
from entrada import Entrada
from saida import Saida
from cliente import Cliente

def abrir_tela_cadastro_cliente():

    
    tela = tk.Toplevel(janela)
    tela.title("Cadastro de Cliente")

    label_nome = tk.Label(tela, text="Nome:")
    label_nome.pack(pady=5, padx=10)
    entry_nome = tk.Entry(tela)
    entry_nome.pack(pady=5, padx=10)

    label_cnpj = tk.Label(tela, text="CNPJ:")
    label_cnpj.pack(pady=5, padx=10)
    entry_cnpj = tk.Entry(tela)
    entry_cnpj.pack(pady=5, padx=10)

    label_telefone = tk.Label(tela, text="Telefone:")
    label_telefone.pack(pady=5, padx=10)
    entry_telefone = tk.Entry(tela)
    entry_telefone.pack(pady=5, padx=10)

    label_cpf = tk.Label(tela, text="CPF:")
    label_cpf.pack(pady=5, padx=10)
    entry_cpf = tk.Entry(tela)
    entry_cpf.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def realizar_cadastro():
        nome = entry_nome.get()
        cnpj = entry_cnpj.get()
        telefone = entry_telefone.get()
        cpf = entry_cpf.get()

        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Cliente.novo_cliente(nome, cnpj, cpf, telefone)

    # Adicionar botão de cadastro à tela de cadastro
    botao_realizar_cadastro = tk.Button(tela, text="Realizar Cadastro", command=realizar_cadastro)
    botao_realizar_cadastro.pack(pady=10, padx=10)


def abrir_tela_editar_cliente():
    
    tela = tk.Toplevel(janela)
    tela.title("Edição de Cliente")

    table = ttk.Treeview(tela, columns=(
        'id','nome', 'CNPJ','CPF', 'telefone'), show='headings')
    table.heading('id', text='id')
    table.heading('nome', text='nome')
    table.heading('CNPJ', text='CNPJ')
    table.heading('CPF', text='CPF')
    table.heading('telefone', text='telefone')
    for j in range(5):
        table.column(j, width=100)
    table.pack()

    clientes = Cliente.listar_clientes()
    for cliente in clientes:
        table.insert('', 'end', values=cliente)

    label_nome = tk.Label(tela, text="Nome:")
    label_nome.pack(pady=5, padx=10)
    entry_nome = tk.Entry(tela)
    entry_nome.pack(pady=5, padx=10)

    label_cnpj = tk.Label(tela, text="CNPJ:")
    label_cnpj.pack(pady=5, padx=10)
    entry_cnpj = tk.Entry(tela)
    entry_cnpj.pack(pady=5, padx=10)

    label_telefone = tk.Label(tela, text="Telefone:")
    label_telefone.pack(pady=5, padx=10)
    entry_telefone = tk.Entry(tela)
    entry_telefone.pack(pady=5, padx=10)

    label_cpf = tk.Label(tela, text="CPF:")
    label_cpf.pack(pady=5, padx=10)
    entry_cpf = tk.Entry(tela)
    entry_cpf.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def atualizar_cadastro():
        nome = entry_nome.get()
        cnpj = entry_cnpj.get()
        telefone = entry_telefone.get()
        cpf = entry_cpf.get()

        id = int(table.selection()[0].split('I')[1]) - 1

        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Cliente.atualizar_cliente(clientes[id][0],nome, cnpj, cpf, telefone)

    # Adicionar botão de cadastro à tela de cadastro
    botao_atualizar_cadastro = tk.Button(tela, text="Atualizar Cadastro", command=atualizar_cadastro)
    botao_atualizar_cadastro.pack(pady=10, padx=10)

def abrir_tela_excluir_cliente():
    
    tela = tk.Toplevel(janela)
    tela.title("Exclusão de Cliente")

    table = ttk.Treeview(tela, columns=(
        'id','nome', 'CNPJ','CPF', 'telefone'), show='headings')
    table.heading('id', text='id')
    table.heading('nome', text='nome')
    table.heading('CNPJ', text='CNPJ')
    table.heading('CPF', text='CPF')
    table.heading('telefone', text='telefone')
    for j in range(5):
        table.column(j, width=100)
    table.pack()

    clientes = Cliente.listar_clientes()
    for cliente in clientes:
        table.insert('', 'end', values=cliente)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def excluir_cadastro():
        id = int(table.selection()[0].split('I')[1]) - 1

        tela.destroy()
        

        Cliente.excluir_cliente(clientes[id][0])
    # Adicionar botão de cadastro à tela de cadastro
    botao_excluir_cadastro = tk.Button(tela, text="Excluir Cadastro", command=excluir_cadastro)
    botao_excluir_cadastro.pack(pady=10, padx=10)

def abrir_tela_cadastro_fornecedor():

    
    tela = tk.Toplevel(janela)
    tela.title("Cadastro de Fornecedor")

    label_nome = tk.Label(tela, text="Nome:")
    label_nome.pack(pady=5, padx=10)
    entry_nome = tk.Entry(tela)
    entry_nome.pack(pady=5, padx=10)

    label_cnpj = tk.Label(tela, text="CNPJ:")
    label_cnpj.pack(pady=5, padx=10)
    entry_cnpj = tk.Entry(tela)
    entry_cnpj.pack(pady=5, padx=10)

    label_telefone = tk.Label(tela, text="Telefone:")
    label_telefone.pack(pady=5, padx=10)
    entry_telefone = tk.Entry(tela)
    entry_telefone.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def realizar_cadastro():
        nome = entry_nome.get()
        cnpj = entry_cnpj.get()
        telefone = entry_telefone.get()

        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Fornecedor.novo_fornecedor(nome, cnpj, telefone)

    # Adicionar botão de cadastro à tela de cadastro
    botao_realizar_cadastro = tk.Button(tela, text="Realizar Cadastro", command=realizar_cadastro)
    botao_realizar_cadastro.pack(pady=10, padx=10)


def abrir_tela_editar_fornecedor():
    
    tela = tk.Toplevel(janela)
    tela.title("Edição de Fornecedor")

    table = ttk.Treeview(tela, columns=(
        'id','nome', 'CNPJ', 'telefone'), show='headings')
    table.heading('id', text='id')
    table.heading('nome', text='nome')
    table.heading('CNPJ', text='CNPJ')
    table.heading('telefone', text='telefone')
    for j in range(4):
        table.column(j, width=100)
    table.pack()

    fornecedores = Fornecedor.listar_fornecedores()
    for fornecedor in fornecedores:
        table.insert('', 'end', values=fornecedor)

    label_nome = tk.Label(tela, text="Nome:")
    label_nome.pack(pady=5, padx=10)
    entry_nome = tk.Entry(tela)
    entry_nome.pack(pady=5, padx=10)

    label_cnpj = tk.Label(tela, text="CNPJ:")
    label_cnpj.pack(pady=5, padx=10)
    entry_cnpj = tk.Entry(tela)
    entry_cnpj.pack(pady=5, padx=10)

    label_telefone = tk.Label(tela, text="Telefone:")
    label_telefone.pack(pady=5, padx=10)
    entry_telefone = tk.Entry(tela)
    entry_telefone.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def atualizar_cadastro():
        nome = entry_nome.get()
        cnpj = entry_cnpj.get()
        telefone = entry_telefone.get()

        id = int(table.selection()[0].split('I')[1]) - 1

        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Fornecedor.atualizar_fornecedor(fornecedores[id][0],nome, cnpj, telefone)

    # Adicionar botão de cadastro à tela de cadastro
    botao_atualizar_cadastro = tk.Button(tela, text="Atualizar Cadastro", command=atualizar_cadastro)
    botao_atualizar_cadastro.pack(pady=10, padx=10)

def abrir_tela_excluir_fornecedor():
    
    tela = tk.Toplevel(janela)
    tela.title("Exclusão de Fornecedor")

    table = ttk.Treeview(tela, columns=(
        'id','nome', 'CNPJ', 'telefone'), show='headings')
    table.heading('id', text='id')
    table.heading('nome', text='nome')
    table.heading('CNPJ', text='CNPJ')
    table.heading('telefone', text='telefone')
    for j in range(4):
        table.column(j, width=100)
    table.pack()

    fornecedores = Fornecedor.listar_fornecedores()
    for fornecedor in fornecedores:
        table.insert('', 'end', values=fornecedor)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def excluir_cadastro():
        id = int(table.selection()[0].split('I')[1]) - 1

        tela.destroy()
        

        Fornecedor.excluir_fornecedor(fornecedores[id][0])

    # Adicionar botão de cadastro à tela de cadastro
    botao_excluir_cadastro = tk.Button(tela, text="Excluir Cadastro", command=excluir_cadastro)
    botao_excluir_cadastro.pack(pady=10, padx=10)

def abrir_tela_cadastrar_produto():
    
    tela = tk.Toplevel(janela)
    tela.title("Cadastro de Produto")

    label_tipo = tk.Label(tela, text="Tipo:")
    label_tipo.pack(pady=5, padx=10)
    entry_tipo = tk.Entry(tela)
    entry_tipo.pack(pady=5, padx=10)

    label_valor = tk.Label(tela, text="Valor:")
    label_valor.pack(pady=5, padx=10)
    entry_valor = tk.Entry(tela)
    entry_valor.pack(pady=5, padx=10)

    label_descricao = tk.Label(tela, text="Descrição:")
    label_descricao.pack(pady=5, padx=10)
    entry_descricao = tk.Entry(tela)
    entry_descricao.pack(pady=5, padx=10)

    label_fornecedor = tk.Label(tela, text="Fornecedor:")
    label_fornecedor.pack(pady=5, padx=10)
    entry_fornecedor = tk.Entry(tela)
    entry_fornecedor.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def realizar_cadastro():
        tipo = entry_tipo.get()
        valor = entry_valor.get()
        descricao = entry_descricao.get()
        fornecedor = entry_fornecedor.get()

        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Produto.novo_produto(tipo, valor, descricao, fornecedor)

    # Adicionar botão de cadastro à tela de cadastro
    botao_realizar_cadastro = tk.Button(tela, text="Realizar Cadastro", command=realizar_cadastro)
    botao_realizar_cadastro.pack(pady=10, padx=10)

def abrir_tela_editar_produto():
    
    tela = tk.Toplevel(janela)
    tela.title("Edição de Produto")

    table = ttk.Treeview(tela, columns=(
        'id','tipo', 'valor', 'descricao', 'fornecedor'), show='headings')
    table.heading('id', text='id')
    table.heading('tipo', text='Tipo')
    table.heading('valor', text='Valor')
    table.heading('descricao', text='Descrição')
    table.heading('fornecedor', text='Fornecedor')
    for j in range(5):
        table.column(j, width=100)
    table.pack()

    produtos = Produto.listar_produtos()
    for produto in produtos:
        table.insert('', 'end', values=produto)

    label_tipo = tk.Label(tela, text="Tipo:")
    label_tipo.pack(pady=5, padx=10)
    entry_tipo = tk.Entry(tela)
    entry_tipo.pack(pady=5, padx=10)

    label_valor = tk.Label(tela, text="Valor:")
    label_valor.pack(pady=5, padx=10)
    entry_valor = tk.Entry(tela)
    entry_valor.pack(pady=5, padx=10)

    label_descricao = tk.Label(tela, text="Descrição:")
    label_descricao.pack(pady=5, padx=10)
    entry_descricao = tk.Entry(tela)
    entry_descricao.pack(pady=5, padx=10)

    label_fornecedor = tk.Label(tela, text="Fornecedor:")
    label_fornecedor.pack(pady=5, padx=10)
    entry_fornecedor = tk.Entry(tela)
    entry_fornecedor.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def atualizar_cadastro():
        tipo = entry_tipo.get()
        valor = entry_valor.get()
        descricao = entry_descricao.get()
        fornecedor = entry_fornecedor.get()

        id = int(table.selection()[0].split('I')[1]) -1 
        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Produto.atualizar_produto(produtos[id][0],tipo, valor, descricao, fornecedor)

    # Adicionar botão de cadastro à tela de cadastro
    botao_atualizar_cadastro = tk.Button(tela, text="Atualizar Cadastro", command=atualizar_cadastro)
    botao_atualizar_cadastro.pack(pady=10, padx=10)

def abrir_tela_excluir_produto():
    
    tela = tk.Toplevel(janela)
    tela.title("Exclusão de Produto")

    table = ttk.Treeview(tela, columns=(
        'id','tipo', 'valor', 'descricao', 'fornecedor'), show='headings')
    table.heading('id', text='id')
    table.heading('tipo', text='Tipo')
    table.heading('valor', text='Valor')
    table.heading('descricao', text='Descrição')
    table.heading('fornecedor', text='Fornecedor')
    for j in range(5):
        table.column(j, width=100)
    table.pack()

    produtos = Produto.listar_produtos()
    for produto in produtos:
        table.insert('', 'end', values=produto)


    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def excluir_cadastro():
   
        id = int(table.selection()[0].split('I')[1]) -1 
        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Produto.excluir_produto(produtos[id][0])

    # Adicionar botão de cadastro à tela de cadastro
    botao_excluir_cadastro = tk.Button(tela, text="Excluir Cadastro", command=excluir_cadastro)
    botao_excluir_cadastro.pack(pady=10, padx=10)

def abrir_tela_cadastrar_entrada():
    
    tela = tk.Toplevel(janela)
    tela.title("Cadastro de Entrada")

    label_data = tk.Label(tela, text="Data:")
    label_data.pack(pady=5, padx=10)
    entry_data = tk.Entry(tela)
    entry_data.pack(pady=5, padx=10)

    label_quantidade = tk.Label(tela, text="Quantidade:")
    label_quantidade.pack(pady=5, padx=10)
    entry_quantidade = tk.Entry(tela)
    entry_quantidade.pack(pady=5, padx=10)

    label_produto = tk.Label(tela, text="Produto:")
    label_produto.pack(pady=5, padx=10)
    entry_produto = tk.Entry(tela)
    entry_produto.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def realizar_cadastro():
        data = entry_data.get()
        quantidade = entry_quantidade.get()
        produto = entry_produto.get()

        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Entrada.nova_entrada(data, quantidade, produto)

    # Adicionar botão de cadastro à tela de cadastro
    botao_realizar_cadastro = tk.Button(tela, text="Realizar Cadastro", command=realizar_cadastro)
    botao_realizar_cadastro.pack(pady=10, padx=10)

def abrir_tela_cadastrar_venda():
    
    tela = tk.Toplevel(janela)
    tela.title("Cadastro de Venda")

    label_data = tk.Label(tela, text="Data:")
    label_data.pack(pady=5, padx=10)
    entry_data = tk.Entry(tela)
    entry_data.pack(pady=5, padx=10)

    label_quantidade = tk.Label(tela, text="Quantidade:")
    label_quantidade.pack(pady=5, padx=10)
    entry_quantidade = tk.Entry(tela)
    entry_quantidade.pack(pady=5, padx=10)

    label_produto = tk.Label(tela, text="Produto:")
    label_produto.pack(pady=5, padx=10)
    entry_produto = tk.Entry(tela)
    entry_produto.pack(pady=5, padx=10)

    label_cliente = tk.Label(tela, text="Cliente:")
    label_cliente.pack(pady=5, padx=10)
    entry_cliente = tk.Entry(tela)
    entry_cliente.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def realizar_cadastro():
        data = entry_data.get()
        quantidade = entry_quantidade.get()
        produto = entry_produto.get()
        cliente = entry_cliente.get()

        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Saida.nova_saida(data, quantidade, produto, cliente)

    # Adicionar botão de cadastro à tela de cadastro
    botao_realizar_cadastro = tk.Button(tela, text="Realizar Cadastro", command=realizar_cadastro)
    botao_realizar_cadastro.pack(pady=10, padx=10)

def abrir_tela_excluir_venda():
    
    tela = tk.Toplevel(janela)
    tela.title("Exclusão de Produto")

    table = ttk.Treeview(tela, columns=(
        'id','data', 'quantidade', 'produto', 'cliente'), show='headings')
    table.heading('id', text='id')
    table.heading('data', text='Data')
    table.heading('quantidade', text='Quantidade')
    table.heading('produto', text='Produto')
    table.heading('cliente', text='Cliente')
    for j in range(5):
        table.column(j, width=100)
    table.pack()

    saidas = Saida.listar_saidas()
    for saida in saidas:
        table.insert('', 'end', values=saida)


    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def excluir_cadastro():
   
        id = int(table.selection()[0].split('I')[1]) -1 
        tela.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Saida.excluir_saida(saidas[id][0])

    # Adicionar botão de cadastro à tela de cadastro
    botao_excluir_cadastro = tk.Button(tela, text="Excluir Cadastro", command=excluir_cadastro)
    botao_excluir_cadastro.pack(pady=10, padx=10)

def abrir_tela_pesquisar_produto():
    
    tela = tk.Toplevel(janela)
    tela.title("Pesquisa de Produto")

    table = ttk.Treeview(tela, columns=(
        'id','tipo', 'valor', 'descricao', 'fornecedor'), show='headings')
    table.heading('id', text='id')
    table.heading('tipo', text='Tipo')
    table.heading('valor', text='Valor')
    table.heading('descricao', text='Descrição')
    table.heading('fornecedor', text='Fornecedor')
    for j in range(5):
        table.column(j, width=100)
    table.pack()
    
    label_pesquisa = tk.Label(tela, text="Pesquisa:")
    label_pesquisa.pack(pady=5, padx=10)
    entry_pesquisa = tk.Entry(tela)
    entry_pesquisa.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def pesquisar():
        pesquisa = entry_pesquisa.get()
        table.delete(*table.get_children())
        Produto.pesquisar_produto(pesquisa)
        produtos = Produto.pesquisar_produto(pesquisa)
        for produto in produtos:
            table.insert('', 'end', values=produto)

    # Adicionar botão de cadastro à tela de cadastro
    botao_pesquisar = tk.Button(tela, text="Pesquisar", command=pesquisar)
    botao_pesquisar.pack(pady=10, padx=10)

    

    

def abrir_tela_resumo_venda():
    
    tela = tk.Toplevel(janela)
    tela.title("Resumo Venda")

    table = ttk.Treeview(tela, columns=(
        'id','tipo', 'valor', 'produto', 'cliente'), show='headings')
    table.heading('id', text='id')
    table.heading('tipo', text='Tipo')
    table.heading('quantidade', text='Quantidade')
    table.heading('produto', text='Produto')
    table.heading('cliente', text='Cliente')
    for j in range(5):
        table.column(j, width=100)
    table.pack()

    saidas = Saida.listar_saidas()
    for saida in saidas:
        table.insert('', 'end', values=saida)

    total = 0
    totalPrice = 0

    for saida in saidas:
      total += saida[2]
      produto = Produto.buscar_produto(saida[3])
      totalPrice += produto[2] * saida[2]

    texto = "Número de vendas: " + str(total) + "\n" + "Valor Arrecadado: " + str(totalPrice)

    label_vendas = tk.Label(tela, text=texto)
    label_vendas.pack(pady=5, padx=10)


def abrir_tela_resumo_fornecedor():
    
    tela = tk.Toplevel(janela)
    tela.title("Exclusão de Fornecedor")

    table = ttk.Treeview(tela, columns=(
        'id','nome', 'CNPJ', 'telefone'), show='headings')
    table.heading('id', text='id')
    table.heading('nome', text='nome')
    table.heading('CNPJ', text='CNPJ')
    table.heading('telefone', text='telefone')
    for j in range(4):
        table.column(j, width=100)
    table.pack()

    fornecedores = Fornecedor.listar_fornecedores()
    for fornecedor in fornecedores:
        table.insert('', 'end', values=fornecedor)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def atualizar_resumo():
        id = int(table.selection()[0].split('I')[1]) - 1
        table2.delete(*table2.get_children())
        saidas = Saida.resumo_fornecedor(fornecedores[id][0])
        for saida in saidas:
            table2.insert('', 'end', values=saida)

        total = 0
        totalPrice = 0
        for saida in saidas:
            total += saida[2]
            produto = Produto.buscar_produto(saida[3])
            totalPrice += produto[2] * saida[2]

        texto = "Número de vendas: " + str(total) + "\n" + "Valor Arrecadado: " + str(totalPrice)
        label_vendas['text'] = texto

    #adicionar botao tk
    botao_resumo_fornecedor = tk.Button(tela, text="Resumo", command=atualizar_resumo)
    botao_resumo_fornecedor.pack(pady=10, padx=10)

    table2 = ttk.Treeview(tela, columns=(
        'id','tipo', 'quantidade', 'produto', 'cliente'), show='headings')
    table2.heading('id', text='id')
    table2.heading('tipo', text='Tipo')
    table2.heading('quantidade', text='Quantidade')
    table2.heading('produto', text='Produto')
    table2.heading('cliente', text='Cliente')
    for j in range(5):
        table2.column(j, width=100)
    table2.pack()



    label_vendas = tk.Label(tela)
    label_vendas.pack(pady=5, padx=10)
    

def abrir_tela_administrador():
    
    tela_administrador = tk.Toplevel(janela)
    tela_administrador.title("Tela de Administrador")


    # Adicionar botão cadastro fornecedor
    botao_cadastro_fornecedor = tk.Button(tela_administrador, text="Cadastro Fornecedor", command=abrir_tela_cadastro_fornecedor)
    botao_cadastro_fornecedor.pack(pady=10, padx=10)

    #Adicionar botão cadastro cliente
    botao_cadastro_cliente = tk.Button(tela_administrador, text="Cadastro Cliente", command=abrir_tela_cadastro_cliente)
    botao_cadastro_cliente.pack(pady=10, padx=10)

    #Adicionar botão edição cliente, exclusão cliente
    botao_editar_cliente = tk.Button(tela_administrador, text="Editar Cliente", command=abrir_tela_editar_cliente)
    botao_editar_cliente.pack(pady=10, padx=10)

    botao_excluir_cliente = tk.Button(tela_administrador, text="Excluir Cliente", command=abrir_tela_excluir_cliente)
    botao_excluir_cliente.pack(pady=10, padx=10)

    #Adicionar botão edição fornecedor, exclusão fornecedor, Cadastrar produto, Editar Produto, Excluir Produto, Cadastrar entrada, Cadastrar venda, Excluir Venda, Pesquisa Produto, Resumo venda, resumo fornecedor
    botao_editar_fornecedor = tk.Button(tela_administrador, text="Editar Fornecedor", command=abrir_tela_editar_fornecedor)
    botao_editar_fornecedor.pack(pady=10, padx=10)

    botao_excluir_fornecedor = tk.Button(tela_administrador, text="Excluir Fornecedor", command=abrir_tela_excluir_fornecedor)
    botao_excluir_fornecedor.pack(pady=10, padx=10)

    botao_cadastrar_produto = tk.Button(tela_administrador, text="Cadastrar Produto", command=abrir_tela_cadastrar_produto)
    botao_cadastrar_produto.pack(pady=10, padx=10)

    botao_editar_produto = tk.Button(tela_administrador, text="Editar Produto", command=abrir_tela_editar_produto)
    botao_editar_produto.pack(pady=10, padx=10)

    botao_excluir_produto = tk.Button(tela_administrador, text="Excluir Produto", command=abrir_tela_excluir_produto)
    botao_excluir_produto.pack(pady=10, padx=10)

    botao_cadastrar_entrada = tk.Button(tela_administrador, text="Cadastrar Entrada", command=abrir_tela_cadastrar_entrada)
    botao_cadastrar_entrada.pack(pady=10, padx=10)

    botao_cadastrar_venda = tk.Button(tela_administrador, text="Cadastrar Venda", command=abrir_tela_cadastrar_venda)
    botao_cadastrar_venda.pack(pady=10, padx=10)

    botao_excluir_venda = tk.Button(tela_administrador, text="Excluir Venda", command=abrir_tela_excluir_venda)
    botao_excluir_venda.pack(pady=10, padx=10)

    botao_pesquisar_produto = tk.Button(tela_administrador, text="Pesquisar Produto", command=abrir_tela_pesquisar_produto)
    botao_pesquisar_produto.pack(pady=10, padx=10)

    botao_resumo_venda = tk.Button(tela_administrador, text="Resumo Venda", command=abrir_tela_resumo_venda)
    botao_resumo_venda.pack(pady=10, padx=10)

    botao_resumo_fornecedor = tk.Button(tela_administrador, text="Resumo Fornecedor", command=abrir_tela_resumo_fornecedor)
    botao_resumo_fornecedor.pack(pady=10, padx=10)


def abrir_tela_estoque():
    
    tela_administrador = tk.Toplevel(janela)
    tela_administrador.title("Tela de Gerente de Estoque")


    botao_cadastrar_produto = tk.Button(tela_administrador, text="Cadastrar Produto", command=abrir_tela_cadastrar_produto)
    botao_cadastrar_produto.pack(pady=10, padx=10)

    botao_editar_produto = tk.Button(tela_administrador, text="Editar Produto", command=abrir_tela_editar_produto)
    botao_editar_produto.pack(pady=10, padx=10)

    botao_excluir_produto = tk.Button(tela_administrador, text="Excluir Produto", command=abrir_tela_excluir_produto)
    botao_excluir_produto.pack(pady=10, padx=10)

    botao_cadastrar_entrada = tk.Button(tela_administrador, text="Cadastrar Entrada", command=abrir_tela_cadastrar_entrada)
    botao_cadastrar_entrada.pack(pady=10, padx=10)

def abrir_tela_venda():
    
    tela_administrador = tk.Toplevel(janela)
    tela_administrador.title("Tela de Gerente de Venda")



    botao_cadastrar_venda = tk.Button(tela_administrador, text="Cadastrar Venda", command=abrir_tela_cadastrar_venda)
    botao_cadastrar_venda.pack(pady=10, padx=10)

    botao_excluir_venda = tk.Button(tela_administrador, text="Excluir Venda", command=abrir_tela_excluir_venda)
    botao_excluir_venda.pack(pady=10, padx=10)


def abrir_tela_login():
    # Criar uma nova janela para a tela de login
    
    tela_login = tk.Toplevel(janela)
    tela_login.title("Tela de Login")

    # Adicionar campos de entrada (Entry) para nome de usuário e senha
    label_usuario = tk.Label(tela_login, text="Nome de Usuário:")
    label_usuario.pack(pady=5, padx=10)
    entry_usuario = tk.Entry(tela_login)
    entry_usuario.pack(pady=5, padx=10)

    label_senha = tk.Label(tela_login, text="Senha:")
    label_senha.pack(pady=5, padx=10)
    entry_senha = tk.Entry(tela_login, show="*")  # A opção show="*" mascara a senha
    entry_senha.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de login na tela de login é pressionado
    def realizar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        

        usuario = Usuario.autenticar(usuario, senha) 
      
        if usuario:
          tela_login.destroy()

          if usuario[3] == "Administrador":
            abrir_tela_administrador()
            

          elif usuario[3] == "Estoque":
            abrir_tela_estoque()
            

          elif usuario[3] == "Venda":
            abrir_tela_venda()
            
        # Torna a janela principal visível novamente
        

  

    # Adicionar botão de login à tela de login
    botao_realizar_login = tk.Button(tela_login, text="Realizar Login", command=realizar_login)
    botao_realizar_login.pack(pady=10, padx=10)

def abrir_tela_cadastro():
    # Criar uma nova janela para a tela de cadastro
    
    tela_cadastro = tk.Toplevel(janela)
    tela_cadastro.title("Tela de Cadastro")

    # Adicionar campos de entrada (Entry) para cadastro
    label_novo_usuario = tk.Label(tela_cadastro, text="Novo Nome de Usuário:")
    label_novo_usuario.pack(pady=5, padx=10)
    entry_novo_usuario = tk.Entry(tela_cadastro)
    entry_novo_usuario.pack(pady=5, padx=10)

    label_nova_senha = tk.Label(tela_cadastro, text="Nova Senha:")
    label_nova_senha.pack(pady=5, padx=10)
    entry_nova_senha = tk.Entry(tela_cadastro, show="*")
    entry_nova_senha.pack(pady=5, padx=10)

    label_cargo = tk.Label(tela_cadastro, text="Cargo:")
    label_cargo.pack(pady=5, padx=10)
    cargos = ["Administrador", "Estoque", "Venda"]
    cargo_selecionada = tk.StringVar()
    dropdown_cargo = tk.OptionMenu(tela_cadastro, cargo_selecionada, *cargos)
    dropdown_cargo.pack(pady=5, padx=10)

    # Função para ser chamada quando o botão de cadastro na tela de cadastro é pressionado
    def realizar_cadastro():
        novo_usuario = entry_novo_usuario.get()
        nova_senha = entry_nova_senha.get()
        cargo = cargo_selecionada.get()

        print(novo_usuario, nova_senha, cargo)

        tela_cadastro.destroy()

        # Torna a janela principal visível novamente
        

        # Adicione sua lógica de cadastro aqui
        Usuario.novo_usuario(novo_usuario, nova_senha, cargo)

    # Adicionar botão de cadastro à tela de cadastro
    botao_realizar_cadastro = tk.Button(tela_cadastro, text="Realizar Cadastro", command=realizar_cadastro)
    botao_realizar_cadastro.pack(pady=10, padx=10)

# Criando a janela principal
janela = tk.Tk()
janela.title("Tela de Login e Cadastro")

# Adicionando botões à janela
botao_login = tk.Button(janela, text="Login", command=abrir_tela_login)
botao_login.pack(pady=10, padx=10)

botao_cadastro = tk.Button(janela, text="Cadastro", command=abrir_tela_cadastro)
botao_cadastro.pack(pady=10, padx=10)

# Iniciando o loop principal da interface gráfica
janela.mainloop()
