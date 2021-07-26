# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaCadastroLogin.ui'
#
# Created: Fri May 31 20:27:16 2019
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

class Ui_TelaCadastroLogin(object):
    def setupUi(self, TelaCadastroLogin):
        TelaCadastroLogin.setObjectName(_fromUtf8("TelaCadastroLogin"))
        TelaCadastroLogin.resize(850, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaCadastroLogin.sizePolicy().hasHeightForWidth())
        TelaCadastroLogin.setSizePolicy(sizePolicy)
        TelaCadastroLogin.setMinimumSize(QtCore.QSize(850, 500))
        TelaCadastroLogin.setMaximumSize(QtCore.QSize(850, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/icone.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        TelaCadastroLogin.setWindowIcon(icon)
        self.Cadastrar = QtGui.QWidget(TelaCadastroLogin)
        self.Cadastrar.setObjectName(_fromUtf8("Cadastrar"))
        self.PlanodeFundo = QtGui.QPushButton(self.Cadastrar)
        self.PlanodeFundo.setGeometry(QtCore.QRect(-10, -4, 871, 519))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.PlanodeFundo.setFont(font)
        self.PlanodeFundo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PlanodeFundo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.PlanodeFundo.setAcceptDrops(True)
        self.PlanodeFundo.setAutoFillBackground(False)
        self.PlanodeFundo.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/grr.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.PlanodeFundo.setIcon(icon1)
        self.PlanodeFundo.setIconSize(QtCore.QSize(850, 600))
        self.PlanodeFundo.setShortcut(_fromUtf8(""))
        self.PlanodeFundo.setAutoRepeat(False)
        self.PlanodeFundo.setAutoExclusive(False)
        self.PlanodeFundo.setAutoDefault(False)
        self.PlanodeFundo.setFlat(True)
        self.PlanodeFundo.setObjectName(_fromUtf8("PlanodeFundo"))
        self.Cadastro = QtGui.QPushButton(self.Cadastrar)
        self.Cadastro.setEnabled(False)
        self.Cadastro.setGeometry(QtCore.QRect(344, 98, 169, 125))
        self.Cadastro.setMouseTracking(True)
        self.Cadastro.setAutoFillBackground(False)
        self.Cadastro.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/IconeCadastro.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/IconeCadastro.png")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/IconeCadastro.png")), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.Cadastro.setIcon(icon2)
        self.Cadastro.setIconSize(QtCore.QSize(130, 130))
        self.Cadastro.setCheckable(False)
        self.Cadastro.setChecked(False)
        self.Cadastro.setAutoRepeat(True)
        self.Cadastro.setAutoExclusive(True)
        self.Cadastro.setAutoRepeatDelay(0)
        self.Cadastro.setAutoRepeatInterval(0)
        self.Cadastro.setAutoDefault(False)
        self.Cadastro.setDefault(False)
        self.Cadastro.setFlat(True)
        self.Cadastro.setObjectName(_fromUtf8("Cadastro"))
        self.btn_Cadastro = QtGui.QPushButton(self.Cadastrar)
        self.btn_Cadastro.setGeometry(QtCore.QRect(340, 410, 165, 48))
        self.btn_Cadastro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Cadastro.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_Cadastro.setAutoFillBackground(False)
        self.btn_Cadastro.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_cadastro.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Cadastro.setIcon(icon3)
        self.btn_Cadastro.setIconSize(QtCore.QSize(160, 160))
        self.btn_Cadastro.setFlat(True)
        self.btn_Cadastro.setObjectName(_fromUtf8("btn_Cadastro"))
        self.IconeSair = QtGui.QPushButton(self.Cadastrar)
        self.IconeSair.setEnabled(True)
        self.IconeSair.setGeometry(QtCore.QRect(12, 12, 41, 39))
        self.IconeSair.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/Icone sair.png")), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/Icone sair.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.IconeSair.setIcon(icon4)
        self.IconeSair.setIconSize(QtCore.QSize(30, 30))
        self.IconeSair.setFlat(True)
        self.IconeSair.setObjectName(_fromUtf8("IconeSair"))
        self.label_2 = QtGui.QLabel(self.Cadastrar)
        self.label_2.setGeometry(QtCore.QRect(336, 384, 173, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Book Antiqua\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Caixa_Senha = QtGui.QLineEdit(self.Cadastrar)
        self.Caixa_Senha.setGeometry(QtCore.QRect(240, 282, 375, 33))
        self.Caixa_Senha.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 233);\n"
"font: 14pt \"Bahnschrift\";"))
        self.Caixa_Senha.setEchoMode(QtGui.QLineEdit.Password)
        self.Caixa_Senha.setAlignment(QtCore.Qt.AlignCenter)
        self.Caixa_Senha.setDragEnabled(False)
        self.Caixa_Senha.setReadOnly(False)
        self.Caixa_Senha.setObjectName(_fromUtf8("Caixa_Senha"))
        self.Caixa_SuperUser = QtGui.QLineEdit(self.Cadastrar)
        self.Caixa_SuperUser.setGeometry(QtCore.QRect(240, 336, 375, 33))
        self.Caixa_SuperUser.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 233);\n"
"font: 14pt \"Bahnschrift\";"))
        self.Caixa_SuperUser.setFrame(True)
        self.Caixa_SuperUser.setEchoMode(QtGui.QLineEdit.Password)
        self.Caixa_SuperUser.setAlignment(QtCore.Qt.AlignCenter)
        self.Caixa_SuperUser.setDragEnabled(False)
        self.Caixa_SuperUser.setReadOnly(False)
        self.Caixa_SuperUser.setObjectName(_fromUtf8("Caixa_SuperUser"))
        self.Caixa_Usuario = QtGui.QLineEdit(self.Cadastrar)
        self.Caixa_Usuario.setGeometry(QtCore.QRect(240, 230, 375, 33))
        self.Caixa_Usuario.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 233);\n"
"font: 14pt \"Bahnschrift\";"))
        self.Caixa_Usuario.setEchoMode(QtGui.QLineEdit.Normal)
        self.Caixa_Usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.Caixa_Usuario.setDragEnabled(False)
        self.Caixa_Usuario.setReadOnly(False)
        self.Caixa_Usuario.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Caixa_Usuario.setObjectName(_fromUtf8("Caixa_Usuario"))
        TelaCadastroLogin.setCentralWidget(self.Cadastrar)

        self.retranslateUi(TelaCadastroLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaCadastroLogin)

    def retranslateUi(self, TelaCadastroLogin):
        TelaCadastroLogin.setWindowTitle(_translate("TelaCadastroLogin", "Cadastrar Usuário", None))
        self.label_2.setText(_translate("TelaCadastroLogin", "*Senha mestre incorreta*", None))
        self.Caixa_Senha.setPlaceholderText(_translate("TelaCadastroLogin", "Senha", None))
        self.Caixa_SuperUser.setPlaceholderText(_translate("TelaCadastroLogin", "Super Mestre", None))
        self.Caixa_Usuario.setPlaceholderText(_translate("TelaCadastroLogin", "Usuário", None))

