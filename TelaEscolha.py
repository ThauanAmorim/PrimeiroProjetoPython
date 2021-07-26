# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaEscolha.ui'
#
# Created: Wed May 29 03:48:21 2019
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

class Ui_TelaEscolha(object):
    def setupUi(self, TelaEscolha):
        TelaEscolha.setObjectName(_fromUtf8("TelaEscolha"))
        TelaEscolha.resize(850, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaEscolha.sizePolicy().hasHeightForWidth())
        TelaEscolha.setSizePolicy(sizePolicy)
        TelaEscolha.setMinimumSize(QtCore.QSize(850, 500))
        TelaEscolha.setMaximumSize(QtCore.QSize(850, 500))
        self.Escolha = QtGui.QWidget(TelaEscolha)
        self.Escolha.setObjectName(_fromUtf8("Escolha"))
        self.PlanodeFundo = QtGui.QPushButton(self.Escolha)
        self.PlanodeFundo.setGeometry(QtCore.QRect(-10, -4, 871, 519))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.PlanodeFundo.setFont(font)
        self.PlanodeFundo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PlanodeFundo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.PlanodeFundo.setAcceptDrops(True)
        self.PlanodeFundo.setAutoFillBackground(False)
        self.PlanodeFundo.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/grr.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.PlanodeFundo.setIcon(icon)
        self.PlanodeFundo.setIconSize(QtCore.QSize(850, 600))
        self.PlanodeFundo.setShortcut(_fromUtf8(""))
        self.PlanodeFundo.setAutoRepeat(False)
        self.PlanodeFundo.setAutoExclusive(False)
        self.PlanodeFundo.setAutoDefault(False)
        self.PlanodeFundo.setFlat(True)
        self.PlanodeFundo.setObjectName(_fromUtf8("PlanodeFundo"))
        self.btn_Visualizar = QtGui.QPushButton(self.Escolha)
        self.btn_Visualizar.setGeometry(QtCore.QRect(112, 368, 259, 63))
        self.btn_Visualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Visualizar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_Visualizar.setAutoFillBackground(False)
        self.btn_Visualizar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Visualizar sem sombras.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Visualizar.setIcon(icon1)
        self.btn_Visualizar.setIconSize(QtCore.QSize(260, 300))
        self.btn_Visualizar.setFlat(True)
        self.btn_Visualizar.setObjectName(_fromUtf8("btn_Visualizar"))
        self.btn_Cadastrar = QtGui.QPushButton(self.Escolha)
        self.btn_Cadastrar.setGeometry(QtCore.QRect(492, 368, 259, 63))
        self.btn_Cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Cadastrar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_Cadastrar.setAutoFillBackground(False)
        self.btn_Cadastrar.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Cadastrar sem sombras.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Cadastrar.setIcon(icon2)
        self.btn_Cadastrar.setIconSize(QtCore.QSize(260, 300))
        self.btn_Cadastrar.setFlat(True)
        self.btn_Cadastrar.setObjectName(_fromUtf8("btn_Cadastrar"))
        self.btn_Logoff = QtGui.QPushButton(self.Escolha)
        self.btn_Logoff.setEnabled(True)
        self.btn_Logoff.setGeometry(QtCore.QRect(34, 28, 61, 63))
        self.btn_Logoff.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/icone_Sair.png")), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/icone_Sair.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Logoff.setIcon(icon3)
        self.btn_Logoff.setIconSize(QtCore.QSize(45, 45))
        self.btn_Logoff.setFlat(True)
        self.btn_Logoff.setObjectName(_fromUtf8("btn_Logoff"))
        self.pushButton = QtGui.QPushButton(self.Escolha)
        self.pushButton.setGeometry(QtCore.QRect(30, 370, 67, 63))
        self.pushButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/icone_Alerta2.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        TelaEscolha.setCentralWidget(self.Escolha)

        self.retranslateUi(TelaEscolha)
        QtCore.QMetaObject.connectSlotsByName(TelaEscolha)

    def retranslateUi(self, TelaEscolha):
        TelaEscolha.setWindowTitle(_translate("TelaEscolha", "Escolha", None))

