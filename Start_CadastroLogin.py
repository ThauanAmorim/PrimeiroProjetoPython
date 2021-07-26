#coding:latin1

import sys
from PyQt4 import QtCore, QtGui, QtTest
from Fachada import FAC_CRIAR_LOGIN, FAC_VERIFICAR_USER_EXISTENTE, FAC_VERIFICADOR_SENHA_MESTRE
from TelaCadastroLogin import Ui_TelaCadastroLogin


class START_TELA_DE_CADASTRAR(QtGui.QMainWindow):
    
    #m�todo para abrir a tela de cadastrar usu�rio
    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaCadastroLogin()
        self.ui.setupUi(self)

        #define o �cone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Cadastro")

        #esconde uma label
        self.ui.label_2.hide()

        #chama o m�todo em pareteses quando o bot�o ou item for clicado
        self.ui.btn_Cadastro.clicked.connect(self.CADASTRAR)
        self.ui.IconeSair.clicked.connect(self.FECHAR_JANELA)



    #m�todo chamado pelo bot�o cadastrar
    def CADASTRAR(self):

        #usuario, senha e senhamestre recebem os textos digitados na tela
        Usuario = (str(self.ui.Caixa_Usuario.text()))
        Senha = (str(self.ui.Caixa_Senha.text()))
        senhaMestre = (str(self.ui.Caixa_SuperUser.text()))


        #verifica se o usu�rio t� em branco
        if Usuario == "":
            #se sim, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Usu�rio est� em branco*")
        #verifica se a senha t� em branco
        elif Senha == "":
            #se sim, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Senha est� em branco*")
        #verifica se a senhamestre t� em branco
        elif senhaMestre == "":
            #se sim, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Senha Mestre est� em branco*")
        #verifica se o usuario j� foi cadastrado anteriormente
        elif FAC_VERIFICAR_USER_EXISTENTE(Usuario):
            #se sim, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Usu�rio j� existente*")
        #verifica se a senha mestre est� correta
        elif FAC_VERIFICADOR_SENHA_MESTRE(senhaMestre):
            #se n�o, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Senha Mestre incorreta*")
        else:
            #envia o usuario, senha e senha mestre para um outro m�todo existente na Fachada, e mostra um texto
            FAC_CRIAR_LOGIN(Usuario, Senha, senhaMestre)
            self.ui.label_2.show()
            self.ui.label_2.setText("*Usuario salvo*")

            #espera 1,5 segundos e fecha a tela
            QtTest.QTest.qWait(1500)
            self.close()
            


    ##m�todo chamado pelo bot�o sair
    def FECHAR_JANELA(self):

        #fecha a pr�pria tela
        self.close()
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_CADASTRAR()
    minhaApp.show()
    sys.exit(app.exec_())
