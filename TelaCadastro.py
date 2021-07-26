# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaCadastro.ui'
#
# Created: Fri May 31 20:22:12 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TelaCadastro(object):
    def setupUi(self, TelaCadastro):
        TelaCadastro.setObjectName(_fromUtf8("TelaCadastro"))
        TelaCadastro.resize(600, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaCadastro.sizePolicy().hasHeightForWidth())
        TelaCadastro.setSizePolicy(sizePolicy)
        TelaCadastro.setMinimumSize(QtCore.QSize(600, 350))
        TelaCadastro.setMaximumSize(QtCore.QSize(600, 350))
        self.JanelaPrincipal = QtGui.QWidget(TelaCadastro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JanelaPrincipal.sizePolicy().hasHeightForWidth())
        self.JanelaPrincipal.setSizePolicy(sizePolicy)
        self.JanelaPrincipal.setObjectName(_fromUtf8("JanelaPrincipal"))
        self.PlanodeFundo = QtGui.QPushButton(self.JanelaPrincipal)
        self.PlanodeFundo.setGeometry(QtCore.QRect(-10, -4, 650, 430))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlanodeFundo.sizePolicy().hasHeightForWidth())
        self.PlanodeFundo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.PlanodeFundo.setFont(font)
        self.PlanodeFundo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PlanodeFundo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.PlanodeFundo.setAcceptDrops(True)
        self.PlanodeFundo.setAutoFillBackground(False)
        self.PlanodeFundo.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/grr segunda tela.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.PlanodeFundo.setIcon(icon)
        self.PlanodeFundo.setIconSize(QtCore.QSize(850, 600))
        self.PlanodeFundo.setShortcut(_fromUtf8(""))
        self.PlanodeFundo.setAutoRepeat(False)
        self.PlanodeFundo.setAutoExclusive(False)
        self.PlanodeFundo.setAutoDefault(False)
        self.PlanodeFundo.setFlat(True)
        self.PlanodeFundo.setObjectName(_fromUtf8("PlanodeFundo"))
        self.NOMEDOPRODUTO = QtGui.QLabel(self.JanelaPrincipal)
        self.NOMEDOPRODUTO.setGeometry(QtCore.QRect(190, 28, 215, 29))
        self.NOMEDOPRODUTO.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"COCOGOOSE \";"))
        self.NOMEDOPRODUTO.setObjectName(_fromUtf8("NOMEDOPRODUTO"))
        self.CODIGOLOTE = QtGui.QLabel(self.JanelaPrincipal)
        self.CODIGOLOTE.setGeometry(QtCore.QRect(144, 120, 147, 29))
        self.CODIGOLOTE.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CODIGOLOTE.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"COCOGOOSE \";"))
        self.CODIGOLOTE.setObjectName(_fromUtf8("CODIGOLOTE"))
        self.VALIDADE = QtGui.QLabel(self.JanelaPrincipal)
        self.VALIDADE.setGeometry(QtCore.QRect(440, 118, 103, 29))
        self.VALIDADE.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.VALIDADE.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"COCOGOOSE \";"))
        self.VALIDADE.setObjectName(_fromUtf8("VALIDADE"))
        self.dateEdit = QtGui.QDateEdit(self.JanelaPrincipal)
        self.dateEdit.setGeometry(QtCore.QRect(414, 156, 151, 33))
        self.dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit.setStyleSheet(_fromUtf8("font: 14pt \"Bahnschrift\";"))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setMaximumDate(QtCore.QDate(2200, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.btn_Salvar = QtGui.QPushButton(self.JanelaPrincipal)
        self.btn_Salvar.setGeometry(QtCore.QRect(200, 252, 201, 61))
        self.btn_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Salvar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Salvar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Salvar.setIcon(icon1)
        self.btn_Salvar.setIconSize(QtCore.QSize(200, 200))
        self.btn_Salvar.setFlat(True)
        self.btn_Salvar.setObjectName(_fromUtf8("btn_Salvar"))
        self.labelAlerta = QtGui.QLabel(self.JanelaPrincipal)
        self.labelAlerta.setGeometry(QtCore.QRect(188, 204, 233, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bahnschrift"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelAlerta.setFont(font)
        self.labelAlerta.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.labelAlerta.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.labelAlerta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelAlerta.setStyleSheet(_fromUtf8("color: rgb(255, 85, 255);\n"
"selection-color: rgb(255, 240, 250);\n"
"font: 16pt \"Bahnschrift\";"))
        self.labelAlerta.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelAlerta.setText(_fromUtf8(""))
        self.labelAlerta.setTextFormat(QtCore.Qt.AutoText)
        self.labelAlerta.setObjectName(_fromUtf8("labelAlerta"))
        self.btn_Voltar = QtGui.QPushButton(self.JanelaPrincipal)
        self.btn_Voltar.setGeometry(QtCore.QRect(26, 12, 53, 33))
        self.btn_Voltar.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Voltar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Voltar.setIcon(icon2)
        self.btn_Voltar.setIconSize(QtCore.QSize(40, 40))
        self.btn_Voltar.setFlat(True)
        self.btn_Voltar.setObjectName(_fromUtf8("btn_Voltar"))
        self.PegarNome = QtGui.QLineEdit(self.JanelaPrincipal)
        self.PegarNome.setGeometry(QtCore.QRect(28, 68, 541, 33))
        self.PegarNome.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 233);\n"
"font: 14pt \"Bahnschrift\";"))
        self.PegarNome.setObjectName(_fromUtf8("PegarNome"))
        self.PegarCodigo = QtGui.QLineEdit(self.JanelaPrincipal)
        self.PegarCodigo.setGeometry(QtCore.QRect(28, 154, 355, 33))
        self.PegarCodigo.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 233);\n"
"font: 14pt \"Bahnschrift\";"))
        self.PegarCodigo.setObjectName(_fromUtf8("PegarCodigo"))
        TelaCadastro.setCentralWidget(self.JanelaPrincipal)

        self.retranslateUi(TelaCadastro)
        QtCore.QMetaObject.connectSlotsByName(TelaCadastro)

    def retranslateUi(self, TelaCadastro):
        TelaCadastro.setWindowTitle(_translate("TelaCadastro", "Pesquisa", None))
        self.NOMEDOPRODUTO.setText(_translate("TelaCadastro", "NOME DO PRODUTO", None))
        self.CODIGOLOTE.setText(_translate("TelaCadastro", "CÓDIGO LOTE", None))
        self.VALIDADE.setText(_translate("TelaCadastro", "VALIDADE", None))

