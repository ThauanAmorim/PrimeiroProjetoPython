#coding:latin1

import sys
from PyQt4 import QtCore, QtGui
from Fachada import FAC_LER_LOGIN, FAC_VERIFICAR_USER_EXISTENTE, FAC_VERIFICADOR_SENHA_MESTRE
from TelaLogin import Ui_TelaLogin
from Start_CadastroLogin import START_TELA_DE_CADASTRAR
from Start_Usuarios import START_TELA_DE_USUARIOS 
from Start_Inicio import START


class START_TELA_DE_LOGIN(QtGui.QMainWindow):
    
    #m�todo para abrir a tela de login
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaLogin()
        self.ui.setupUi(self)

        #define o �cone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Cadastro")

        #esconde alguns bot�es e labels
        self.ui.SenhaMestre.hide()
        self.ui.Login_SenhaMestre.hide()
        self.ui.btn_Ir.hide()
        self.ui.label.hide()
        self.ui.label_2.hide()

        #chama o def em pareteses quando o bot�o for clicado
        self.ui.btn_Login.clicked.connect(self.LOGIN)
        self.ui.btn_Cadastro.clicked.connect(self.ABRIR_CADASTRAR)
        self.ui.IconeSair.clicked.connect(self.FECHAR_APP)
        self.ui.Box_ExcluirCadastros.activated.connect(self.DIGITE_SENHA)
        self.ui.btn_Ir.clicked.connect(self.ABRIR_CADASTROS)


        
    #m�todo chamado pelo bot�o login
    def LOGIN(self):

        #usuario e senha recebem o texto digitado na tela e root recebe nada
        Usuario = (str(self.ui.Login_Usuario.text()))
        Senha = (str(self.ui.Login_Senha.text()))
        root = ""


        #verifica se o usuario est� em branco
        if Usuario ==  "":
            #se sim, mostra um texto
            self.ui.label.show()
            self.ui.label.setText("*Preencha o Usuario em branco*")
        #verifica se a senha est� em branco
        elif Senha == "":
            #se sim, mostra um texto
            self.ui.label.show()
            self.ui.label.setText("*Preencha a Senha em branco*")
        #verifica se o usu�rio existe
        elif FAC_VERIFICAR_USER_EXISTENTE(Usuario):
            #se sim, verifica se dados de login est�o corretos
            if FAC_LER_LOGIN(Usuario, Senha, root):
                #se sim, fecha a pr�pria tela
                self.close()

                #abre a tela inicial
                t = START(self)
                t.show()    
            else:
                #se n�o, mostra um texto
                self.ui.label.show()
                self.ui.label.setText("*Senha incorreta*")
        else:
                #se n�o, mostra um texto
                self.ui.label.show()
                self.ui.label.setText("*Usu�rio n�o existe*")


            
    #m�todo chamado pelo bot�o que abre a tela de cadastro
    def ABRIR_CADASTRAR(self):
        
        t = START_TELA_DE_CADASTRAR(self)
        t.show()



    #m�todo chamado pelo bot�o sair
    def FECHAR_APP(self):

        #fecha a pr�pria tela
        self.close()



    #m�todo chamado pela combobox
    def DIGITE_SENHA(self):

        #esconde a combobox e mostra os bot�es escondidos inicialmente
        self.ui.Box_ExcluirCadastros.hide()
        self.ui.SenhaMestre.show()
        self.ui.Login_SenhaMestre.show()
        self.ui.btn_Ir.show()


        
    #m�todo chamado pelo bot�o ir
    def ABRIR_CADASTROS(self):

        #senha recebe o texto digitado na tela
        senha = (str(self.ui.Login_SenhaMestre.text()))


        #verifica se a senha est� incorreta
        if not FAC_VERIFICADOR_SENHA_MESTRE(senha):
            #se n�o, zera algumas caixas de texto e as esconde
            self.ui.Box_ExcluirCadastros.show()
            self.ui.SenhaMestre.hide()
            self.ui.Login_SenhaMestre.clear()
            self.ui.Login_SenhaMestre.hide()
            self.ui.btn_Ir.hide()

            #abre a tela de usu�rios
            t = START_TELA_DE_USUARIOS(self)
            t.show()
        else:
            #verifica se a senha est� em branco
            if senha == "":
                #se sim, mostra um texto
                self.ui.label_2.show()
                self.ui.label_2.setText("*Senha em branco*")
            #se a senha estiver incorreta
            else:
                #zera a caixa de texto e mostra um texto
                self.ui.Login_SenhaMestre.clear()
                self.ui.label_2.show()
                self.ui.label_2.setText("*Senha mestre incorreta*")
            

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_LOGIN()
    minhaApp.show()
    sys.exit(app.exec_())
