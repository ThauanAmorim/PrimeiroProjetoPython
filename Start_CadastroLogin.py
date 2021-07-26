#coding:latin1

import sys
from PyQt4 import QtCore, QtGui, QtTest
from Fachada import FAC_CRIAR_LOGIN, FAC_VERIFICAR_USER_EXISTENTE, FAC_VERIFICADOR_SENHA_MESTRE
from TelaCadastroLogin import Ui_TelaCadastroLogin


class START_TELA_DE_CADASTRAR(QtGui.QMainWindow):
    
    #método para abrir a tela de cadastrar usuário
    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaCadastroLogin()
        self.ui.setupUi(self)

        #define o ícone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Cadastro")

        #esconde uma label
        self.ui.label_2.hide()

        #chama o método em pareteses quando o botão ou item for clicado
        self.ui.btn_Cadastro.clicked.connect(self.CADASTRAR)
        self.ui.IconeSair.clicked.connect(self.FECHAR_JANELA)



    #método chamado pelo botão cadastrar
    def CADASTRAR(self):

        #usuario, senha e senhamestre recebem os textos digitados na tela
        Usuario = (str(self.ui.Caixa_Usuario.text()))
        Senha = (str(self.ui.Caixa_Senha.text()))
        senhaMestre = (str(self.ui.Caixa_SuperUser.text()))


        #verifica se o usuário tá em branco
        if Usuario == "":
            #se sim, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Usuário está em branco*")
        #verifica se a senha tá em branco
        elif Senha == "":
            #se sim, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Senha está em branco*")
        #verifica se a senhamestre tá em branco
        elif senhaMestre == "":
            #se sim, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Senha Mestre está em branco*")
        #verifica se o usuario já foi cadastrado anteriormente
        elif FAC_VERIFICAR_USER_EXISTENTE(Usuario):
            #se sim, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Usuário já existente*")
        #verifica se a senha mestre está correta
        elif FAC_VERIFICADOR_SENHA_MESTRE(senhaMestre):
            #se não, mostra um texto
            self.ui.label_2.show()
            self.ui.label_2.setText("*Senha Mestre incorreta*")
        else:
            #envia o usuario, senha e senha mestre para um outro método existente na Fachada, e mostra um texto
            FAC_CRIAR_LOGIN(Usuario, Senha, senhaMestre)
            self.ui.label_2.show()
            self.ui.label_2.setText("*Usuario salvo*")

            #espera 1,5 segundos e fecha a tela
            QtTest.QTest.qWait(1500)
            self.close()
            


    ##método chamado pelo botão sair
    def FECHAR_JANELA(self):

        #fecha a própria tela
        self.close()
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_CADASTRAR()
    minhaApp.show()
    sys.exit(app.exec_())
