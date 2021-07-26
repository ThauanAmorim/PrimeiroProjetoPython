#coding:latin1

import sys
from PyQt4 import QtCore, QtGui
from Fachada import FAC_VERIFICADOR
from TelaApreciacao import Ui_TelaApreciar


class START_TELA_DE_APRECIACAO(QtGui.QMainWindow):

    #método para abrir a tela de apreciação
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaApreciar()
        self.ui.setupUi(self)

        #define o ícone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Apreciação")
        
        #esconde as label de aviso
        self.ui.nenhumprodutovencido.hide()
        self.ui.nenhumprodutovencido_2.hide()

        #chama o método em pareteses quando o botão ou item for clicado
        self.ui.btn_Voltar_2.clicked.connect(self.VOLTAR)
        
        #chama o método inicial
        self.PRODUTOS()
        

        
    #método para mostrar na tela inicial todos os produtos cadastrados   
    def PRODUTOS(self):
        
        proximos_de_vencer, vencidos = [], [] #cria duas listas vazias
        proximos_de_vencer, vencidos = FAC_VERIFICADOR() #adiciona nas listas todo o valor de um método da Fachada


        #verifica se uma das listas tem mais de 0 objetoss
        if (len(vencidos)>0):
            #se sim, ele adiciona todos na tela
            for k in range(0, len(vencidos)):
                self.ui.treeWidget_Vencidos.addTopLevelItem(QtGui.QTreeWidgetItem(vencidos[k]))
        else:
            #se não, esconde widget, e uma label, mostra outra label com um texto
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
            #se não, esconde widget,  e uma label, mostra outra label com um texto
            self.ui.produtosparasevencer.hide()
            self.ui.treeWidget_Vencer.hide()
            self.ui.nenhumprodutovencido.show()
            self.ui.nenhumprodutovencido.setText("Nenhum produto perto de se vencer.")
        


    #método chamado pelo botão voltar
    def VOLTAR(self):
        
        #fecha a própria tela
        self.close()

        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_APRECIACAO()
    minhaApp.show()
    sys.exit(app.exec_())
