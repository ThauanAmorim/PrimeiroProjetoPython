#coding:latin1

import sys
from PyQt4 import QtCore, QtGui
from TelaEscolha import Ui_TelaEscolha
from Start_Cadastro import START_TELA_DE_CADASTRO
from Start_Pesquisa import START_TELA_DE_PESQUISA
from Start_Apreciacao import START_TELA_DE_APRECIACAO


class START(QtGui.QMainWindow):

    #m�todo para abrir a tela inicial
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaEscolha()
        self.ui.setupUi(self)
        
        #define o �cone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela Inicial")

        #chama o def em pareteses quando o bot�o for clicado
        self.ui.btn_Cadastrar.clicked.connect(self.ABRIR_TELA_DE_CADASTRO)
        self.ui.btn_Visualizar.clicked.connect(self.ABRIR_TELA_DE_PESQUISA)
        self.ui.pushButton.clicked.connect(self.ABRIR_TELA_DE_APRECIACAO)
        self.ui.btn_Logoff.clicked.connect(self.BOTAO_LOGOFF)
        
        
        
    #m�todo chamado pelo bot�o que abre a tela de cadastro
    def ABRIR_TELA_DE_CADASTRO(self):
        
        t = START_TELA_DE_CADASTRO(self)
        t.show()


        
    #m�todo chamado pelo bot�o que abre a tela de pesquisa
    def ABRIR_TELA_DE_PESQUISA(self):
        
        t = START_TELA_DE_PESQUISA(self)
        t.show()


        
    #m�todo chamado pelo bot�o que abre a tela de aprecia��o
    def ABRIR_TELA_DE_APRECIACAO(self):
        
        t = START_TELA_DE_APRECIACAO(self)
        t.show()



    #m�todo chamado pelo bot�o de sair
    def BOTAO_LOGOFF(self):

        #fecha a pr�pria tela
        self.close()
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START()
    minhaApp.show()
    sys.exit(app.exec_())
