#coding:latin1
import os, random, base64, zipfile

############# LOGIN #############

#encriptador
def ENCODE(arq):
    aux = base64.b64encode(arq)
    return base64.b64encode(aux)
#decriptador
def DECODE(arq):
    aux = base64.b64decode(arq)
    return base64.b64decode(aux) 
#cria varias letras aleatorias 
def RANDOM():
    txt, letras = "", ['=','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, 100):
        for j in range(0, random.randint(11, 20)):
            num = random.randint(0, 52)
            chave = random.randint(1, 5)
            txt += letras[num]
            if(chave == 2):
                txt += "\f"
            elif(chave == 4):
                txt += "\a"
        txt += "\n"
    return txt

def DAO_CRIAR_TELA_EDITAR(produto, lote, validade):
    with open("Estoque/temp.dll","w") as arq:
        arq.write(produto+"\n"+lote+"\n"+validade)

def DAO_LER_TELA_EDITAR(parametro="mostrar"):
    if(os.path.exists("Estoque/temp.dll")):
        with open("Estoque/temp.dll", "r")as arq:
            dados = [linha for linha in arq.readlines()]
        if(parametro == "apagar" or parametro == "APAGAR"):
            os.remove("Estoque/temp.dll")
        return dados[0].replace("\n", ""), dados[1].replace("\n", ""), dados[2]
#verifica se o user ja existe
def DAO_VERIFICAR_USER_EXISTENTE(user):
    user = ENCODE(user)
    if not os.path.exists("Login/"):
        os.makedirs("Login/")
    if os.path.exists("Login/"+ user + ".dll"):
        return True
#verifica se as pastas de login exitem, caso nao ele cria
def DAO_VERIFICAR_LOGIN():
    if not os.path.exists("Login/"):
        os.makedirs("Login/")
    if not os.path.exists("Login/system"):
        os.makedirs("Login/system")
    if not os.path.exists("Login/system/ColorDefault.dll"):
        with open("Login/system/ColorDefault.dll", "w") as arq:
            senha = "admin"
            rep = ENCODE(senha) #senha aki
            txt_list = []
            for i in range(0, len(rep)):
                txt_list.append(rep[i])
                if(i == 2 or i == 5 or i == 9):
                    txt_list.append("\a")
            txt_str = ""
            for i in range(0, len(txt_list)):
                txt_str += txt_list[i]
            txt_str.replace("\a", "")
            txt_str += "\f\n"
            arq.writelines(RANDOM())
            arq.writelines(txt_str)
            arq.writelines(RANDOM())
            arq.writelines(RANDOM())
            arq.writelines(RANDOM())
            arq.writelines(RANDOM())
    if not os.path.exists("Login/Lista_Users.dll"):
        with open("Login/Lista_Users.dll", "w") as arq:
            arq.write("")
#ler a senha do admin
def DAO_LER_SUPER_USER():
    DAO_VERIFICAR_LOGIN()
    with open("Login/system/ColorDefault.dll", "r") as arq:
        lista = [linha for linha in arq.readlines()]
        decode = lista[100]
        return DECODE(decode)
#cria a lista de users
def DAO_CRIAR_LISTA_USERS(user):
    user = ENCODE(user)
    lista = DAO_LER_LISTA_USERS()
    with open("Login/Lista_Users.dll", "w") as arq:
        arq.writelines(lista)
        arq.writelines("{}\n".format(user))
#ler as informações dos users, como senha e login
def DAO_LER_USER(user):
    user = ENCODE(user)
    lista_crip = []
    with open("Login/"+ user + ".dll", "r") as arq:
        lista = [linha for linha in arq.readlines()]
        for i in range(0, len(lista)):
            user = DECODE(lista[i])
            lista_crip.append(user)
    return lista_crip[0], lista_crip[1]
#faz a leitura da lista de todos os users cadastrados
def DAO_LER_LISTA_USERS():
    DAO_VERIFICAR_LOGIN()
    with open("Login/Lista_Users.dll", "r") as arq:
        lista = [linha for linha in arq.readlines()]
        return lista
#faz o login
def DAO_FAZER_LOGIN(user = "", senha = ""):
    lista = DAO_LER_LISTA_USERS()
    for i in range(0, len(lista)):
        user_pc, senha_pc = DAO_LER_USER(user)
        user_pc = user_pc.replace("\n", "")
        
#cria o login, salva nas pastas as informacoes
def DAO_CRIAR_LOGIN(user = "", senha = "", admin = ""):
    DAO_VERIFICAR_LOGIN()
    DAO_CRIAR_LISTA_USERS(user)
    admin_pc = DAO_LER_SUPER_USER()
    user, senha = ENCODE(user), ENCODE(senha)
    with open("Login/" + user + ".dll", "w") as arq:
            arq.write("{}\n{}".format(user, senha))
#exclui um cadastro ja existente
def DAO_EXCLUIR_CADASTRO_LOGIN(user):
    user = ENCODE(user)
    os.remove("Login/"+ user +".dll")
    lista_users = DAO_LER_LISTA_USERS()
    lista_users.remove(user + "\n")
    with open("Login/Lista_Users.dll", "w") as arq:
        arq.writelines(lista_users)


########################    ESTOQUE    ##############################
#verifica se o produto ja existe no pc
def DAO_VERIFICAR_PRODUTO_EXISTENTE(produto):
    produto = ENCODE(produto)
    if not os.path.exists("Estoque/"):
        os.makedirs("Estoque/")
    if os.path.exists("Estoque/"+ produto + ".dll"):
        return True


#cria a lista de estoque
def DAO_CRIAR_LISTA_ESTOQUE(lista):
    DAO_VERIFICAR_LISTA_ESTOQUE()
    lista = ENCODE(lista)
    lista_ler = DAO_LER_LISTA_ESTOQUE()
    with open("Estoque/Lista_Estoque/Lista.dll", "w") as arq:
        arq.writelines(lista_ler)
        arq.writelines(lista)
        arq.writelines("\n")
#ler a lista de estoque
def DAO_LER_LISTA_ESTOQUE():
    DAO_VERIFICAR_LISTA_ESTOQUE()
    lista_descript, saida = [], []
    with open("Estoque/Lista_Estoque/Lista.dll", "r") as arq:
        lista = [linha for linha in arq.readlines()]
        return lista

