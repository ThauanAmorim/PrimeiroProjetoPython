#coding:latin1

import sys
from PyQt4 import QtCore, QtGui, QtTest
from Fachada import FAC_EDITAR_ESTOQUE, FAC_VERIFICAR_DIGITADO, FAC_LER_TELA_EDITAR
from TelaEditar import Ui_TelaEditar


class START_TELA_DE_EDITAR(QtGui.QMainWindow):

    #m�todo para abrir a tela de cadastrar usu�rio
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaEditar()
        self.ui.setupUi(self)

        #define o �cone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Editar")
        
        #chama o def em pareteses quando o bot�o for clicado
        self.ui.btn_Salvar.clicked.connect(self.BOTAO_SALVAR)
        self.ui.btn_Voltar.clicked.connect(self.VOLTAR)

        
        #chama o m�todo inicial
        self.INICIO()



    #m�todo para mostrar os dados do produto selecionado 
    def INICIO (self):

        #vari�veis recebem o valor de um m�todo da Fachada
        produto_ant, lote, val = FAC_LER_TELA_EDITAR("mostrar")
        
        ano = val[-4:] #ano recebe os 4 �ltimos d�gitos do valor
        mes = val[-7 : -5].replace("/", "") #mes recebe os 2 d�gitos anteriores a ano, e substitui a barra por um nada

        
        #verifica se mes � maior ou igual a 2 d�gitos
        if(len(mes) >= 2):
            dia = val[-11 : -8] #se mes tiver 2 d�gitos, dia vai receber 3 digitos anteriores a mes ap�s o espa�o
        else:
            dia = val[-10 : -7] #se mes tiver 1 d�gito, dia vai receber 3 digitos anteriores a mes
            

        #converte a validade para int e mostra na tela todos os dados do produto selecionado
        self.ui.PegarNome.setText(produto_ant)
        self.ui.PegarCodigo.setText(lote)
        self.ui.dateEdit.setDate(QtCore.QDate(int(ano), int(mes), int(dia)))
        
        
        
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
        
        #produto e lote recebem o texto escrito pelo usu�rio na tela e deixa todas em mai�sculo
        produto = (str(self.ui.PegarNome.text()).upper())
        lote = (str(self.ui.PegarCodigo.text()).upper())

        data = self.ui.dateEdit.date() #data recebe a data selecionada pelo usu�rio na tela
        validade = data.toString() #validade recebe a data e converte para string


        #verifica se foi digitado algo na tela  
        if FAC_VERIFICAR_DIGITADO (produto, lote):
            #se n�o, mostra um texto
            self.ui.labelAlerta.setText("Nenhum nome digitado.") #se n�o, escreve essa mensagem na tela, e n�o salva o produto
        else:
            #vari�veis recebem o valor de um m�todo da Fachada
            produto_ant, aa, bb = FAC_LER_TELA_EDITAR("apagar")

            #chama o m�todo anterior para converter data, envia o nome antigo do produto, nome novo do produto, lote e validade (j� convertida) para um outro m�todo existente na Fachada, e mostra um texto       
            FAC_EDITAR_ESTOQUE(str(produto_ant), str(produto), str(lote), str(self.CONVERT_DATA(validade)))
            self.ui.labelAlerta.setText("Produto salvo.")

            #espera 1,5 segundo e fecha a tela
            QtTest.QTest.qWait(1500)
            self.close()


            
    #m�todo chamado pelo bot�o voltar
    def VOLTAR(self):

        #vari�veis recebem o valor de um m�todo da Fachada
        produto_ant, lote, validade = FAC_LER_TELA_EDITAR("apagar")
    
        #fecha a pr�pria tela
        self.close()
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_EDITAR()
    minhaApp.show()
    sys.exit(app.exec_())
