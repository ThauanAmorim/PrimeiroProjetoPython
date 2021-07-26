#coding:latin1
import os, time
from datetime import date, datetime
from DAO import *
#temp de dados de login
def CRIAR_TELA_EDITAR(produto, lote, validade):
    return DAO_CRIAR_TELA_EDITAR(produto, lote, validade)
#temp de dados de login
def LER_TELA_EDITAR(parametro):
    return DAO_LER_TELA_EDITAR(parametro)
#mostra a lista de todos os users
def MOSTRAR_TODOS_USERS():
    saida, aux = [], ""
    lista_users = DAO_LER_LISTA_USERS()
    for i in range(0, len(lista_users)):
        aux = lista_users[i]
        saida.append(DECODE(aux))
    return saida
#ler a leitura do estoque
def LER_ESTOQUE(produto):
    produto = ENCODE(produto)
    return DAO_LER_ESTOQUE(produto)
#edita o estoque
def EDITAR_ESTOQUE(produto_ant, produto, lote, val):
    return DAO_EDITAR_ESTOQUE(produto_ant, produto, lote, val)
#exclui o cadastro de login
def EXCLUIR_CADASTRO_LOGIN(user):
    return DAO_EXCLUIR_CADASTRO_LOGIN(user)
#verifica se o user existe
def VERIFICAR_USER_EXISTENTE(user):
    return DAO_VERIFICAR_USER_EXISTENTE(user)
#verifica a senha mestre
def VERIFICADOR_SENHA_MESTRE(senha):
    if(senha == DAO_LER_SUPER_USER()):
        return False
    else:
        return True
#cria o login
def CRIAR_LOGIN(user, senha, root):
    VERIFICAR_DIGITADO_USER(user, senha, root)
    DAO_CRIAR_LOGIN(user, senha)
#ler o login
def LER_LOGIN(user, senha, root = ""):
    usuario_pc, senha_pc = DAO_LER_USER(user) 
    usuario_pc = usuario_pc.replace("\n", "")
    if(user == usuario_pc and senha == senha_pc):
        return True
    else:
        return False
#cria o estoque de produtos
def CRIAR_ESTOQUE(produto = "", lote = "", validade = ""): 
    VERIFICAR_DIGITADO(produto, lote)
    CRIAR_LISTA_ESTOQUE(produto)
    DAO_CRIAR_ESTOQUE (produto, lote, validade)
#verifica se o produto existe
def VERIFICAR_PRODUTO_EXISTENTE(produto): 
    return DAO_VERIFICAR_PRODUTO_EXISTENTE(produto)
#verifica se tem algo digitado
def VERIFICAR_DIGITADO_USER(user = "", senha = "", root = ""):
    if(user == "" or senha == "" or root == ""):
        return True
#verifica se n foi digitado nada
def VERIFICAR_DIGITADO(produto, lote): 
    if(produto == ""):
        return True
    if(lote == ""):
        return True
#verifica se o produto existe
def VERIFICAR_PRODUTO_EXISTENTE(produto): 
    return DAO_VERIFICAR_PRODUTO_EXISTENTE(produto)
#vai comparar a data salva com a data do pc pra fazer verificacao diaria
def COMPARAR(): 
    data_pc = DAO_LER_DATA()
    data_atual = DATA_CONV()
    time.sleep(60) #tempo para a proxima verifica��o
    if (data_pc == data_atual):
        return False
    else:
        return True
#converte data em str
def DATA_CONV(): 
    data_atual = date.today()
    data_pc = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
    return data_pc
#cria a lista dos produtos criados
def CRIAR_LISTA_ESTOQUE(produto): 
    DAO_CRIAR_LISTA_ESTOQUE(produto)
#tempo pra verificar, meses, dias, e tals
def TEMPO_VERIFICACAO(antecedencia = 15):
    DAO_CRIAR_DATA_ANT(antecedencia)
#converte uma str em type date
def DATA_VERIFICACAO(data_prod): 
    data = data_prod
    data = datetime.strptime(data, '%d/%m/%Y').date()
    data_antecedencia = date.fromordinal(data.toordinal() - int(DAO_LER_DATA_ANT()))
    data_convertida = "{}/{}/{}".format(data_antecedencia.day, data_antecedencia.month, data_antecedencia.year)
    return data_convertida
#cria a data de vencimento
def DATA_RESTANTE(val): 
    valor = val
    valor = datetime.strptime(valor, '%d/%m/%Y').date()
    data_restante = valor - date.today()
    return data_restante.days
#converte a str data em date type
def CONVERTER_STR_DATA(numero):
    str_date = numero
    date = datetime.strptime(str_date, '%d/%m/%Y').date()
    return date
#verifica se o produto ta vencido
def VERIFICADOR(): 
    lista_pc = DAO_LER_LISTA_ESTOQUE()
    saida, lista, cont, lista_alerta, lista_vencidos = [], [], 0, [], []
    for i in range(0, len(lista_pc)):
        sla = lista_pc[i]
        sla = sla.replace("\n", "")
        saida.append(sla)
    lista_produtos_alerta, lista_produtos_vencidos = [], []
    for i in range(0, len(saida)):
        if(os.path.exists("Estoque/"+ saida[i] + ".dll")):
            produto, lote, validade = DAO_LER_ESTOQUE(saida[i])
            if(CONVERTER_STR_DATA(DATA_CONV()) >= CONVERTER_STR_DATA(DATA_VERIFICACAO(validade)) and CONVERTER_STR_DATA(DATA_CONV()) < CONVERTER_STR_DATA(validade)):
                lista += DAO_LER_ESTOQUE(saida[i].replace("\n", ""))
                lista.append(DATA_RESTANTE(validade))
                nome_produto = lista[cont].replace("\n", "")
                lote = lista[cont+1].replace("\n", "")
                validade = lista[cont+2].replace("\n", "")
                dias_rest = str(lista[cont+3])
                segunda_lista = nome_produto, lote, validade, dias_rest
                lista_alerta.append(segunda_lista)
                cont += 4
            if(DATA_RESTANTE(validade)<= 0):
                lista += DAO_LER_ESTOQUE(saida[i].replace("\n", ""))
                nome_produto = lista[cont].replace("\n", "")
                lote = lista[cont+1].replace("\n", "")
                validade = lista[cont+2]
                segunda_lista = nome_produto, lote, validade
                lista_vencidos.append(segunda_lista)
                cont += 3
        else:
            pass
    return lista_alerta, lista_vencidos
#mostra a lista de todos os produtos cadastrados
def TODOS_PRODUTOS():
    cont, lista, segunda_lista, lista_mostrar= 0, [], "", []
    lista_produtos = DAO_LER_LISTA_ESTOQUE()
    for i in range(0, len(lista_produtos)):
        lista += DAO_LER_ESTOQUE(lista_produtos[i].replace("\n", ""))
        nome_produto = lista[cont].replace("\n", "")
        lote = lista[cont+1].replace("\n", "")
        validade = lista[cont+2]
        segunda_lista = nome_produto, lote, validade
        lista_mostrar.append(segunda_lista)
        cont += 3
    return lista_mostrar
#mostra os produtos que está proximo de vencer 
def TODOS_PRODUTOS_ALERTA():
    cont, lista, segunda_lista, lista_mostrar= 0, [], "", []
    lista_produtos = DAO_LER_LISTA_ESTOQUE()
    for i in range(0, len(lista_produtos)):
        lista += DAO_LER_ESTOQUE(lista_produtos[i].replace("\n", ""))
        nome_produto = lista[cont].replace("\n", "")
        lote = lista[cont+1].replace("\n", "")
        validade = lista[cont+2]
        segunda_lista = nome_produto, lote, validade
        lista_mostrar.append(segunda_lista)
        cont += 3

    return lista_mostrar
#metodo q apaga os produtos
def APAGAR_PRODUTO(produto):
    produto = ENCODE(produto)
    lista_estoque = DAO_LER_LISTA_ESTOQUE()
    if(os.path.exists("Estoque/"+ produto + ".dll")):
        os.remove("Estoque/"+ produto + ".dll")
        lista_estoque.remove(str(produto)+"\n")
        DAO_SALVAR_ARQ_APOS_APAGAR(lista_estoque)

def SEPARAR_CARACTERES(txt):
    lista1 = []
    for i in range(0, len(txt)):
        lista1 += txt[i]
    return lista1

def JUNTAR_CARACTERES(txt):
    lista = ""
    for i in range(0, len(txt)):
        lista += str(txt[i])
    return lista

#barra de pesquisa
def BARRA_PESQUISA(produto):
    lista1, saida, lista_todos_produtos, lista_pesquisa, lista_produtos = [], [], [], [], []
    DAO_VERIFICAR_ESTOQUE()
    DAO_VERIFICAR_LISTA_ESTOQUE()
    lista_produtos_cript = DAO_LER_LISTA_ESTOQUE()
    for i in lista_produtos_cript:
        lista_produtos.append(DECODE(i.replace("\n", "")))
    for i in range(0, len(lista_produtos)):
        aux = lista_produtos[i]
        for j in range(0, len(aux)):
            lista1 += aux[j]
        saida.append(lista1) # separa os produtos por caracteres  // Arraylist de arraylist, o segundo arraylist receb os caracteres
        lista1 = []
    letras = []
    for i in range(0, len(saida)):
        for j in SEPARAR_CARACTERES(produto):
            letras += j # arraylist de caracteres
            if(j in saida[i]): #se oq foi digitado contem nas letras do obj
                if(produto in JUNTAR_CARACTERES(saida[i])):
                    lista_todos_produtos.append(JUNTAR_CARACTERES(saida[i]))
                    break
    for i in range(0, len(lista_todos_produtos)):
        produtos = DAO_LER_ESTOQUE(ENCODE(lista_todos_produtos[i]))
        nome_produto = produtos[0].replace("\n", "")
        lote = produtos[1].replace("\n", "")
        validade = produtos[2].replace("\n", "")
        dados = nome_produto, lote, validade
        lista_pesquisa.append(dados)
    return lista_pesquisa


#onde organiza os metodos
def PRINCIPAL(): 
    DAO_VERIFICAR_DATA()
    DAO_CRIAR_DATA(DATA_CONV())
    while True:
        time.sleep(10)
        if(COMPARAR()):
            DAO_CRIAR_DATA(DATA_CONV())
            VERIFICADOR()
        else:
            pass