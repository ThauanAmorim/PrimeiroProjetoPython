#coding:latin1

import sys
from PyQt4 import QtCore, QtGui
from Fachada import FAC_BARRA_PESQUISA, FAC_TODOS_PRODUTOS, FAC_TEMPO_VERIFICACAO, FAC_APAGAR_PRODUTO, FAC_CRIAR_TELA_EDITAR, FAC_VERIFICAR_PRODUTO_EXISTENTE
from TelaPesquisa import Ui_TelaPesquisa
from Start_Apreciacao import START_TELA_DE_APRECIACAO
from Start_Editar import START_TELA_DE_EDITAR


class START_TELA_DE_PESQUISA(QtGui.QMainWindow):

    #método para abrir a tela de pesquisa
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaPesquisa()
        self.ui.setupUi(self)

        #define o ícone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Pesquisa")
        
        #esconde o botão apagar e a label de aviso
        self.ui.btn_Apagar.hide()
        self.ui.semProduto.hide()
        self.ui.btn_Editar.hide()

        #chama o método em pareteses quando o botão ou item for clicado
        self.ui.btn_Verificar.clicked.connect(self.BOTAO_VERIFICAR)
        self.ui.treeWidget.itemClicked.connect(self.SELECIONADO)
        self.ui.btn_OK.clicked.connect(self.NOTIFICAR)
        self.ui.btn_Apagar.clicked.connect(self.APAGAR)
        self.ui.btn_Pesquisar.clicked.connect(self.PESQUISAR)
        self.ui.btn_Voltar_2.clicked.connect(self.VOLTAR)
        self.ui.btn_Editar.clicked.connect(self.EDITAR)
        
        #chama o método inicial
        self.TODOS_PRODUTOS()

        
        
    #método para mostrar todos os produtos cadastrados na tela inicial
    def TODOS_PRODUTOS(self):
        
        lista_produtos = [] #cria uma lista vazia
        lista_produtos = FAC_TODOS_PRODUTOS() #adiciona na lista todo o valor de um método da Fachada

        
        #verifica se a lista tem mais de 0 objetos
        if (len(lista_produtos)>0):
            #se sim, ele adiciona todos na tela
            for k in range(0, len(lista_produtos)):
                self.ui.treeWidget.addTopLevelItem(QtGui.QTreeWidgetItem(lista_produtos[k]))
        else:
            #se não, esconde botão apagar, verificar e editar, widget inicial e mostra uma mensagem na tela
            self.ui.btn_Apagar.hide()
            self.ui.btn_Editar.hide()
            self.ui.btn_Verificar.hide()
            self.ui.treeWidget.hide()
            self.ui.semProduto.show()
            self.ui.semProduto.setText("NENHUM PRODUTO ENCONTRADO.")


            
    #método chamado pelo botão pesquisar
    def PESQUISAR(self):
        
        #produto recebe o texto escrito pelo usuário na tela e deixa todas em maiúsculo
        produto = (str(self.ui.BarraPesquisa.text()).upper())


        #verifica se o produto digitado existe em um método da Fachada
        if not (FAC_VERIFICAR_PRODUTO_EXISTENTE(produto) == True):
            #se não, ele mostra uma mensagem e esconde botão apagar
            self.ui.btn_Apagar.hide()
            self.ui.btn_Editar.hide()
            self.ui.treeWidget.hide()
            self.ui.semProduto.show()
            self.ui.semProduto.setText("NENHUM PRODUTO ENCONTRADO.")
        else:
            #se sim, ele esconde o botão apagar e editar, zera a tela inicial e adiciona apenas o produto pesquisado
            self.ui.semProduto.hide()
            self.ui.btn_Apagar.hide()
            self.ui.btn_Editar.hide()
            self.ui.treeWidget.show()
            self.ui.treeWidget.clear()
            
            lista_produtos = [] #cria uma lista vazia
            lista_produtos = FAC_BARRA_PESQUISA(produto) #adiciona na lista todo o valor de um método da Fachada
            
        
            #adiciona todos produtos na tela
            for k in range(0, len(lista_produtos)):
                self.ui.treeWidget.addTopLevelItem(QtGui.QTreeWidgetItem(lista_produtos[k]))
                

            
    #método chamado quando um item é selecionado
    def SELECIONADO(self):
        
        self.ui.btn_Apagar.show() #mostra na tela o botão de apagar item
        self.ui.btn_Editar.show() #mostra na tela o botão de editar item
        selecionado = self.ui.treeWidget.selectedItems() #selecionado recebe o item selecionado

        #retorna selecionado pra o método, para ser usado em outro método
        return selecionado



    #método chamado pelo botão apagar
    def APAGAR(self):
        
        #produto recebe o valor do método selecionado e envia para um método da Fachada convertendo-o para string
        nome = self.SELECIONADO()
        lista = nome[0]
        produto = lista.text(0)
        FAC_APAGAR_PRODUTO(str(produto))
        
        #zera a tela inicial e chama o metodo inicial
        self.ui.treeWidget.clear()
        self.TODOS_PRODUTOS()

        #esconde os botões de apagar e editar
        self.ui.btn_Apagar.hide()
        self.ui.btn_Editar.hide()



    #método chamado pelo botão ok
    def NOTIFICAR(self):
        
        #tempo recebe o número digitado pelo usuário na tela e envia para um método da Fachada
        tempo = self.ui.box_Notificar.value()
        FAC_TEMPO_VERIFICACAO(tempo)



    #método chamado pelo botão verificar
    def BOTAO_VERIFICAR(self):
        
        #abre a tela de apreciação
        t = START_TELA_DE_APRECIACAO(self)
        t.show()
        


    #método chamado pelo botão voltar
    def VOLTAR(self):
        
        #fecha a própria tela
        self.close()

        

    #método chamado pelo botão editar
    def EDITAR(self):
        
        #produto_ant, lote e val recebem o valor do método selecionado e envia para um método da Fachada convertendo-os para string
        nome = self.SELECIONADO()
        lista = nome[0]
        produto_ant = lista.text(0)
        lote = lista.text(1)
        val = lista.text(2)
        FAC_CRIAR_TELA_EDITAR(str(produto_ant), str(lote), str(val))

        #abre a tela de cadastro
        t = START_TELA_DE_EDITAR(self)
        t.show()  

        #esconde os botões de apagar e editar
        self.ui.btn_Apagar.hide()
        self.ui.btn_Editar.hide()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_PESQUISA()
    minhaApp.show()
    sys.exit(app.exec_())
