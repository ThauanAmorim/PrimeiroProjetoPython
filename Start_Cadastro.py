#coding:latin1

import sys
from PyQt4 import QtCore, QtGui, QtTest
from Fachada import FAC_CRIAR_ESTOQUE, FAC_VERIFICAR_PRODUTO_EXISTENTE, FAC_VERIFICAR_DIGITADO
from TelaCadastro import Ui_TelaCadastro


class START_TELA_DE_CADASTRO(QtGui.QMainWindow):
    
    #m�todo para abrir a tela de cadastro
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaCadastro()
        self.ui.setupUi(self)

        #define o �cone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Cadastro")
        
        #definindo a data atual na tela
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
        
        #chama o m�todo em pareteses quando o bot�o for clicado
        self.ui.btn_Salvar.clicked.connect(self.BOTAO_SALVAR)
        self.ui.btn_Voltar.clicked.connect(self.VOLTAR)

        
        
    #m�todo para converter a data para dd/mm/yyyy
    def CONVERT_DATA(self, valor):

        #biblioteca para salvar todos os meses em n�meros
        meses = {'jan':1, 'fev':2, 'mar':3, 'abr':4, 'mai':5, 'jun':6, 'jul':7, 'ago':8, 'set':9, 'out':10, 'nov':11, 'dez':12}

        ano = valor[-4:] #ano recebe os 4 �ltimos d�gitos do valor
        dia = valor[-7 : -5].replace(" ", "") #dia recebe os 2 d�gitos anteriores a ano, caso o dia tenha apenas um digito, substitui o espa�o por um nada


        #verifica se dia � maior ou igual a 2 d�gitos
        if(len(dia) >= 2):
            mes = valor[-11 : -8] #se dia tiver 2 d�gitos, mes vai receber 3 digitos anteriores a dia ap�s o espa�o
        else:
            mes = valor[-10 : -7] #se dia tiver 1 d�gito, mes vai receber 3 digitos anteriores a dia


        #converte o mes recebido em str para um num da biblioteca e retorna dia, mes(j�convertido) e ano para o m�todo, para ser usado em outro m�todo            
        return "{}/{}/{}".format(dia, meses[str(mes)], ano)


        
    #m�todo chamado pelo bot�o salvar
    def BOTAO_SALVAR(self):
        
        #produto e lote recebem o texto digitados na tela e deixa todas em mai�sculo
        produto = (str(self.ui.PegarNome.text()).upper())
        lote = (str(self.ui.PegarCodigo.text()).upper())

        data = self.ui.dateEdit.date() #data recebe a data selecionada pelo usu�rio na tela
        validade = data.toString() #validade recebe a data e converte para string


        #verifica se o produto j� existe
        if (FAC_VERIFICAR_PRODUTO_EXISTENTE(produto) == True):
            #se sim, mostra um texto
            self.ui.labelAlerta.setText("*Produto j� existente*") #se sim, escreve essa mensagem na tela, e n�o salva o produto
        #verifica se foi digitado algo na tela  
        elif FAC_VERIFICAR_DIGITADO (produto, lote):
            #se n�o, mostra um texto
            self.ui.labelAlerta.setText("*Algo est� em branco*") #se n�o, escreve essa mensagem na tela, e n�o salva o produto
        else:
            #chama o m�todo anterior para converter data, envia o nome do produto, lote e validade (j� convertida) para um outro m�todo existente na Fachada, e mostra um texto
            FAC_CRIAR_ESTOQUE(produto, lote, self.CONVERT_DATA(validade)) 
            self.ui.labelAlerta.setText("*Produto salvo*")

            #zera as caixas de texto
            self.ui.PegarNome.clear()
            self.ui.PegarCodigo.clear()

            #espera 1,5 segundos e apaga o texto anteriormente mostrado
            QtTest.QTest.qWait(1500)
            self.ui.labelAlerta.setText("")



    #m�todo chamado pelo bot�o voltar
    def VOLTAR(self):
        
        #fecha a pr�pria tela
        self.close()

        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_CADASTRO()
    minhaApp.show()
    sys.exit(app.exec_())
