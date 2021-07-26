#coding:latin1

import sys
from PyQt4 import QtCore, QtGui, QtTest
from Fachada import FAC_EDITAR_ESTOQUE, FAC_VERIFICAR_DIGITADO, FAC_LER_TELA_EDITAR
from TelaEditar import Ui_TelaEditar


class START_TELA_DE_EDITAR(QtGui.QMainWindow):

    #método para abrir a tela de cadastrar usuário
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaEditar()
        self.ui.setupUi(self)

        #define o ícone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Editar")
        
        #chama o def em pareteses quando o botão for clicado
        self.ui.btn_Salvar.clicked.connect(self.BOTAO_SALVAR)
        self.ui.btn_Voltar.clicked.connect(self.VOLTAR)

        
        #chama o método inicial
        self.INICIO()



    #método para mostrar os dados do produto selecionado 
    def INICIO (self):

        #variáveis recebem o valor de um método da Fachada
        produto_ant, lote, val = FAC_LER_TELA_EDITAR("mostrar")
        
        ano = val[-4:] #ano recebe os 4 últimos dígitos do valor
        mes = val[-7 : -5].replace("/", "") #mes recebe os 2 dígitos anteriores a ano, e substitui a barra por um nada

        
        #verifica se mes é maior ou igual a 2 dígitos
        if(len(mes) >= 2):
            dia = val[-11 : -8] #se mes tiver 2 dígitos, dia vai receber 3 digitos anteriores a mes após o espaço
        else:
            dia = val[-10 : -7] #se mes tiver 1 dígito, dia vai receber 3 digitos anteriores a mes
            

        #converte a validade para int e mostra na tela todos os dados do produto selecionado
        self.ui.PegarNome.setText(produto_ant)
        self.ui.PegarCodigo.setText(lote)
        self.ui.dateEdit.setDate(QtCore.QDate(int(ano), int(mes), int(dia)))
        
        
        
    #método para converter a data para dd/mm/yyyy
    def CONVERT_DATA(self, valor):

        #biblioteca para salvar todos os meses em números
        meses = {'jan':1, 'fev':2, 'mar':3, 'abr':4, 'mai':5, 'jun':6, 'jul':7, 'ago':8, 'set':9, 'out':10, 'nov':11, 'dez':12}

        ano = valor[-4:] #ano recebe os 4 últimos dígitos do valor
        dia = valor[-7 : -5].replace(" ", "") #dia recebe os 2 dígitos anteriores a ano, caso o dia tenha apenas um digito, substitui o espaço por um nada


        #verifica se dia é maior ou igual a 2 dígitos
        if(len(dia) >= 2):
            mes = valor[-11 : -8] #se dia tiver 2 dígitos, mes vai receber 3 digitos anteriores a dia após o espaço
        else:
            mes = valor[-10 : -7] #se dia tiver 1 dígito, mes vai receber 3 digitos anteriores a dia


        #converte o mes recebido em str para um num da biblioteca e retorna dia, mes(jáconvertido) e ano para o método, para ser usado em outro método            
        return "{}/{}/{}".format(dia, meses[str(mes)], ano)



    #método chamado pelo botão salvar
    def BOTAO_SALVAR(self):
        
        #produto e lote recebem o texto escrito pelo usuário na tela e deixa todas em maiúsculo
        produto = (str(self.ui.PegarNome.text()).upper())
        lote = (str(self.ui.PegarCodigo.text()).upper())

        data = self.ui.dateEdit.date() #data recebe a data selecionada pelo usuário na tela
        validade = data.toString() #validade recebe a data e converte para string


        #verifica se foi digitado algo na tela  
        if FAC_VERIFICAR_DIGITADO (produto, lote):
            #se não, mostra um texto
            self.ui.labelAlerta.setText("Nenhum nome digitado.") #se não, escreve essa mensagem na tela, e não salva o produto
        else:
            #variáveis recebem o valor de um método da Fachada
            produto_ant, aa, bb = FAC_LER_TELA_EDITAR("apagar")

            #chama o método anterior para converter data, envia o nome antigo do produto, nome novo do produto, lote e validade (já convertida) para um outro método existente na Fachada, e mostra um texto       
            FAC_EDITAR_ESTOQUE(str(produto_ant), str(produto), str(lote), str(self.CONVERT_DATA(validade)))
            self.ui.labelAlerta.setText("Produto salvo.")

            #espera 1,5 segundo e fecha a tela
            QtTest.QTest.qWait(1500)
            self.close()


            
    #método chamado pelo botão voltar
    def VOLTAR(self):

        #variáveis recebem o valor de um método da Fachada
        produto_ant, lote, validade = FAC_LER_TELA_EDITAR("apagar")
    
        #fecha a própria tela
        self.close()
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_EDITAR()
    minhaApp.show()
    sys.exit(app.exec_())
