#coding:latin1

import sys
from PyQt4 import QtCore, QtGui
from Fachada import FAC_MOSTRAR_TODOS_USERS, FAC_EXCLUIR_CADASTRO_LOGIN
from TelaExcluirLogin import Ui_TelaUsuarios


class START_TELA_DE_USUARIOS(QtGui.QMainWindow):

    #método para abrir a tela de usuários
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaUsuarios()
        self.ui.setupUi(self)

        #define o ícone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Usuários")
        
        #esconde uma label e um botão
        self.ui.semUsuarios.hide()
        self.ui.btn_Apagar.hide()
        
        #chama o def em pareteses quando o botão for clicado
        self.ui.btn_Voltar_2.clicked.connect(self.BOTAO_VOLTAR)
        self.ui.treeWidget_Users.itemClicked.connect(self.SELECIONADO)
        self.ui.btn_Apagar.clicked.connect(self.APAGAR)

        #chama o método inicial
        self.TODOS_USUARIOS()

        
        
    #método para mostrar todos os produtos cadastrados na tela inicial
    def TODOS_USUARIOS(self):
        
        lista_usuarios = FAC_MOSTRAR_TODOS_USERS() #adiciona na lista todo o valor de um método da Fachada


        #verifica se a lista tem mais de 0 objetos
        if (len(lista_usuarios)>0):
            #se sim, ele adiciona todos na tela
            for i in range(0, len(lista_usuarios)):
                self.ui.treeWidget_Users.addTopLevelItem(QtGui.QTreeWidgetItem(lista_usuarios[i:]))
        else:
            #se não, esconde botão apagar, verificar e editar, widget inicial e mostra uma mensagem na tela
            self.ui.btn_Apagar.hide()
            self.ui.treeWidget_Users.hide()
            self.ui.usuarios.hide()
            self.ui.semUsuarios.show()
            self.ui.semUsuarios.setText("NENHUM USUÁRIO ENCONTRADO.")



    #método chamado pelo botão voltar
    def BOTAO_VOLTAR(self):

        #fecha a própria tela
        self.close()

        

    #método chamado quando um item é selecionado
    def SELECIONADO(self):

        self.ui.btn_Apagar.show() #mostra na tela o botão de apagar item
        selecionado = self.ui.treeWidget_Users.selectedItems() #selecionado recebe o item selecionado


        #retorna selecionado pra o método, para ser usado em outro método
        return selecionado



    #método chamado pelo botão apagar
    def APAGAR(self):
        
        #user recebe o valor do método selecionado e envia para um método da Fachada convertendo-o para string
        nome = self.SELECIONADO()
        lista = nome[0]
        user = lista.text(0)
        FAC_EXCLUIR_CADASTRO_LOGIN(str(user))
        
        #zera a tela inicial e chama o metodo inicial
        self.ui.treeWidget_Users.clear()
        self.TODOS_USUARIOS()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_USUARIOS()
    minhaApp.show()
    sys.exit(app.exec_())
