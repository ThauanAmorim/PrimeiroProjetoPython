# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaEditar.ui'
#
# Created: Fri May 31 20:31:51 2019
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

class Ui_TelaEditar(object):
    def setupUi(self, TelaEditar):
        TelaEditar.setObjectName(_fromUtf8("TelaEditar"))
        TelaEditar.resize(600, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaEditar.sizePolicy().hasHeightForWidth())
        TelaEditar.setSizePolicy(sizePolicy)
        TelaEditar.setMinimumSize(QtCore.QSize(600, 350))
        TelaEditar.setMaximumSize(QtCore.QSize(600, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/icone.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        TelaEditar.setWindowIcon(icon)
        self.Editar = QtGui.QWidget(TelaEditar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Editar.sizePolicy().hasHeightForWidth())
        self.Editar.setSizePolicy(sizePolicy)
        self.Editar.setObjectName(_fromUtf8("Editar"))
        self.PlanodeFundo = QtGui.QPushButton(self.Editar)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/grr segunda tela.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.PlanodeFundo.setIcon(icon1)
        self.PlanodeFundo.setIconSize(QtCore.QSize(850, 600))
        self.PlanodeFundo.setShortcut(_fromUtf8(""))
        self.PlanodeFundo.setAutoRepeat(False)
        self.PlanodeFundo.setAutoExclusive(False)
        self.PlanodeFundo.setAutoDefault(False)
        self.PlanodeFundo.setFlat(True)
        self.PlanodeFundo.setObjectName(_fromUtf8("PlanodeFundo"))
        self.NOMEDOPRODUTO = QtGui.QLabel(self.Editar)
        self.NOMEDOPRODUTO.setGeometry(QtCore.QRect(190, 28, 215, 29))
        self.NOMEDOPRODUTO.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"COCOGOOSE \";"))
        self.NOMEDOPRODUTO.setObjectName(_fromUtf8("NOMEDOPRODUTO"))
        self.CODIGOLOTE = QtGui.QLabel(self.Editar)
        self.CODIGOLOTE.setGeometry(QtCore.QRect(144, 120, 147, 29))
        self.CODIGOLOTE.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CODIGOLOTE.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"COCOGOOSE \";"))
        self.CODIGOLOTE.setObjectName(_fromUtf8("CODIGOLOTE"))
        self.VALIDADE = QtGui.QLabel(self.Editar)
        self.VALIDADE.setGeometry(QtCore.QRect(440, 118, 103, 29))
        self.VALIDADE.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.VALIDADE.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"COCOGOOSE \";"))
        self.VALIDADE.setObjectName(_fromUtf8("VALIDADE"))
        self.dateEdit = QtGui.QDateEdit(self.Editar)
        self.dateEdit.setGeometry(QtCore.QRect(414, 156, 151, 33))
        self.dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit.setStyleSheet(_fromUtf8("font: 14pt \"Bahnschrift\";"))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.dateEdit.setDate(QtCore.QDate(2019, 5, 3))
        self.dateEdit.setMaximumDate(QtCore.QDate(2200, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.btn_Salvar = QtGui.QPushButton(self.Editar)
        self.btn_Salvar.setGeometry(QtCore.QRect(200, 258, 201, 61))
        self.btn_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Salvar.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Salvar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Salvar.setIcon(icon2)
        self.btn_Salvar.setIconSize(QtCore.QSize(200, 200))
        self.btn_Salvar.setFlat(True)
        self.btn_Salvar.setObjectName(_fromUtf8("btn_Salvar"))
        self.labelAlerta = QtGui.QLabel(self.Editar)
        self.labelAlerta.setGeometry(QtCore.QRect(190, 214, 233, 27))
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
        self.btn_Voltar = QtGui.QPushButton(self.Editar)
        self.btn_Voltar.setGeometry(QtCore.QRect(26, 12, 53, 33))
        self.btn_Voltar.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Voltar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Voltar.setIcon(icon3)
        self.btn_Voltar.setIconSize(QtCore.QSize(40, 40))
        self.btn_Voltar.setFlat(True)
        self.btn_Voltar.setObjectName(_fromUtf8("btn_Voltar"))
        self.PegarCodigo = QtGui.QLineEdit(self.Editar)
        self.PegarCodigo.setGeometry(QtCore.QRect(26, 156, 355, 33))
        self.PegarCodigo.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 233);\n"
"font: 14pt \"Bahnschrift\";"))
        self.PegarCodigo.setObjectName(_fromUtf8("PegarCodigo"))
        self.PegarNome = QtGui.QLineEdit(self.Editar)
        self.PegarNome.setGeometry(QtCore.QRect(28, 70, 541, 33))
        self.PegarNome.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 233);\n"
"font: 14pt \"Bahnschrift\";"))
        self.PegarNome.setObjectName(_fromUtf8("PegarNome"))
        TelaEditar.setCentralWidget(self.Editar)

        self.retranslateUi(TelaEditar)
        QtCore.QMetaObject.connectSlotsByName(TelaEditar)

    def retranslateUi(self, TelaEditar):
        TelaEditar.setWindowTitle(_translate("TelaEditar", "Editar", None))
        self.NOMEDOPRODUTO.setText(_translate("TelaEditar", "NOME DO PRODUTO", None))
        self.CODIGOLOTE.setText(_translate("TelaEditar", "CÓDIGO LOTE", None))
        self.VALIDADE.setText(_translate("TelaEditar", "VALIDADE", None))

