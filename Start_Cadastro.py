#coding:latin1

import sys
from PyQt4 import QtCore, QtGui, QtTest
from Fachada import FAC_CRIAR_ESTOQUE, FAC_VERIFICAR_PRODUTO_EXISTENTE, FAC_VERIFICAR_DIGITADO
from TelaCadastro import Ui_TelaCadastro


class START_TELA_DE_CADASTRO(QtGui.QMainWindow):
    
    #método para abrir a tela de cadastro
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TelaCadastro()
        self.ui.setupUi(self)

        #define o ícone e o nome da janela
        self.setWindowIcon(QtGui.QIcon("Imagens/icone.png"))
        self.setWindowTitle("Tela de Cadastro")
        
        #definindo a data atual na tela
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
        
        #chama o método em pareteses quando o botão for clicado
        self.ui.btn_Salvar.clicked.connect(self.BOTAO_SALVAR)
        self.ui.btn_Voltar.clicked.connect(self.VOLTAR)

        
        
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
        
        #produto e lote recebem o texto digitados na tela e deixa todas em maiúsculo
        produto = (str(self.ui.PegarNome.text()).upper())
        lote = (str(self.ui.PegarCodigo.text()).upper())

        data = self.ui.dateEdit.date() #data recebe a data selecionada pelo usuário na tela
        validade = data.toString() #validade recebe a data e converte para string


        #verifica se o produto já existe
        if (FAC_VERIFICAR_PRODUTO_EXISTENTE(produto) == True):
            #se sim, mostra um texto
            self.ui.labelAlerta.setText("*Produto já existente*") #se sim, escreve essa mensagem na tela, e não salva o produto
        #verifica se foi digitado algo na tela  
        elif FAC_VERIFICAR_DIGITADO (produto, lote):
            #se não, mostra um texto
            self.ui.labelAlerta.setText("*Algo está em branco*") #se não, escreve essa mensagem na tela, e não salva o produto
        else:
            #chama o método anterior para converter data, envia o nome do produto, lote e validade (já convertida) para um outro método existente na Fachada, e mostra um texto
            FAC_CRIAR_ESTOQUE(produto, lote, self.CONVERT_DATA(validade)) 
            self.ui.labelAlerta.setText("*Produto salvo*")

            #zera as caixas de texto
            self.ui.PegarNome.clear()
            self.ui.PegarCodigo.clear()

            #espera 1,5 segundos e apaga o texto anteriormente mostrado
            QtTest.QTest.qWait(1500)
            self.ui.labelAlerta.setText("")



    #método chamado pelo botão voltar
    def VOLTAR(self):
        
        #fecha a própria tela
        self.close()

        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    minhaApp = START_TELA_DE_CADASTRO()
    minhaApp.show()
    sys.exit(app.exec_())
