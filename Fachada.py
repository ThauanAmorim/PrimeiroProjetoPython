#coding:latin1

from Servicos import CRIAR_ESTOQUE, VERIFICAR_PRODUTO_EXISTENTE, VERIFICAR_DIGITADO, BARRA_PESQUISA, TODOS_PRODUTOS, TEMPO_VERIFICACAO, APAGAR_PRODUTO, VERIFICADOR, CRIAR_LOGIN, LER_LOGIN, VERIFICADOR_SENHA_MESTRE, VERIFICAR_USER_EXISTENTE, EDITAR_ESTOQUE, MOSTRAR_TODOS_USERS, EXCLUIR_CADASTRO_LOGIN, CRIAR_TELA_EDITAR, LER_TELA_EDITAR


def FAC_CRIAR_ESTOQUE(produto, lote, validade):
    return CRIAR_ESTOQUE(produto, lote, validade)

def FAC_VERIFICAR_PRODUTO_EXISTENTE(produto):
    return VERIFICAR_PRODUTO_EXISTENTE(produto)

def FAC_VERIFICAR_DIGITADO (produto, lote):
    return VERIFICAR_DIGITADO (produto, lote)

def FAC_BARRA_PESQUISA(produto):
    return BARRA_PESQUISA(produto)

def FAC_TODOS_PRODUTOS():
    return TODOS_PRODUTOS()

def FAC_TEMPO_VERIFICACAO(tempo):
    return TEMPO_VERIFICACAO(tempo)

def FAC_APAGAR_PRODUTO(produto):
    return APAGAR_PRODUTO(produto)
    print FAC_APAGAR_PRODUTO(produto)

def FAC_VERIFICADOR():
    return VERIFICADOR()

def FAC_CRIAR_LOGIN(user, senha, root):
    return CRIAR_LOGIN(user, senha, root)

def FAC_LER_LOGIN(user, senha, root = "so pra n dar erro"):
    return LER_LOGIN(user, senha, root = "so pra n dar erro")

def FAC_VERIFICADOR_SENHA_MESTRE(senha):
    return VERIFICADOR_SENHA_MESTRE(senha)

def FAC_VERIFICAR_USER_EXISTENTE(user):
    return  VERIFICAR_USER_EXISTENTE(user)

def FAC_EDITAR_ESTOQUE(produto_ant, produto, lote, val):
    return EDITAR_ESTOQUE(produto_ant, produto, lote, val)

def FAC_MOSTRAR_TODOS_USERS():
    return MOSTRAR_TODOS_USERS()

def FAC_EXCLUIR_CADASTRO_LOGIN(user):
    return EXCLUIR_CADASTRO_LOGIN(user)

def FAC_CRIAR_TELA_EDITAR(produto, lote, validade):
    return CRIAR_TELA_EDITAR(produto, lote, validade)

def FAC_LER_TELA_EDITAR(parametro):
    return LER_TELA_EDITAR(parametro)

