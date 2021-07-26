#coding:latin1

import sys
from PyQt4 import QtCore, QtGui
from Fachada import FAC_VERIFICADOR
from TelaApreciacao import Ui_TelaApreciar


class START_TELA_DE_APRECIACAO(QtGui.QMainWindow):

    #m�todo para abrir a tela de aprecia��o
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaApreciar()
        self.ui.setupUi(self)

        #define o �cone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Aprecia��o")
        
        #esconde as label de aviso
        self.ui.nenhumprodutovencido.hide()
        self.ui.nenhumprodutovencido_2.hide()

        #chama o m�todo em pareteses quando o bot�o ou item for clicado
        self.ui.btn_Voltar_2.clicked.connect(self.VOLTAR)
        
        #chama o m�todo inicial
        self.PRODUTOS()
        

        
    #m�todo para mostrar na tela inicial todos os produtos cadastrados   
    def PRODUTOS(self):
        
        proximos_de_vencer, vencidos = [], [] #cria duas listas vazias
        proximos_de_vencer, vencidos = FAC_VERIFICADOR() #adiciona nas listas todo o valor de um m�todo da Fachada


        #verifica se uma das listas tem mais de 0 objetoss
        if (len(vencidos)>0):
            #se sim, ele adiciona todos na tela
            for k in range(0, len(vencidos)):
                self.ui.treeWidget_Vencidos.addTopLevelItem(QtGui.QTreeWidgetItem(vencidos[k]))
        else:
            #se n�o, esconde widget, e uma label, mostra outra label com um texto
            self.ui.produtosvencidos.hide()
            self.ui.treeWidget_Vencidos.hide()
            self.ui.nenhumprodutovencido_2.show()
            self.ui.nenhumprodutovencido_2.setText("Nenhum produto vencido.")
            
  
        #verifica a outra lista tem mais de 0 objetos
        if (len(proximos_de_vencer)>0):
            #se sim, ele adiciona todos na tela
            for k in range(0, len(proximos_de_vencer)):
                self.ui.treeWidget_Vencer.addTopLevelItem(QtGui.QTreeWidgetItem(proximos_de_vencer[k]))
        else:
            #se n�o, esconde widget,  e uma label, mostra outra label com um texto
            self.ui.produtosparasevencer.hide()
            self.ui.treeWidget_Vencer.hide()
            self.ui.nenhumprodutovencido.show()
            self.ui.nenhumprodutovencido.setText("Nenhum produto perto de se vencer.")
        


    #m�todo chamado pelo bot�o voltar
    def VOLTAR(self):
        
        #fecha a pr�pria tela
        self.close()

        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_APRECIACAO()
    minhaApp.show()
    sys.exit(app.exec_())
