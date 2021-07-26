# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaLogin.ui'
#
# Created: Fri May 31 20:50:02 2019
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

class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName(_fromUtf8("TelaLogin"))
        TelaLogin.resize(850, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaLogin.sizePolicy().hasHeightForWidth())
        TelaLogin.setSizePolicy(sizePolicy)
        TelaLogin.setMinimumSize(QtCore.QSize(850, 500))
        TelaLogin.setMaximumSize(QtCore.QSize(850, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/icone.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        TelaLogin.setWindowIcon(icon)
        self.Logar = QtGui.QWidget(TelaLogin)
        self.Logar.setObjectName(_fromUtf8("Logar"))
        self.PlanodeFundo = QtGui.QPushButton(self.Logar)
        self.PlanodeFundo.setGeometry(QtCore.QRect(-10, -10, 871, 519))
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
        self.User = QtGui.QPushButton(self.Logar)
        self.User.setEnabled(False)
        self.User.setGeometry(QtCore.QRect(338, 58, 169, 125))
        self.User.setMouseTracking(True)
        self.User.setAutoFillBackground(False)
        self.User.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/user.png")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.User.setIcon(icon2)
        self.User.setIconSize(QtCore.QSize(130, 130))
        self.User.setCheckable(False)
        self.User.setChecked(False)
        self.User.setAutoRepeat(True)
        self.User.setAutoExclusive(True)
        self.User.setAutoRepeatDelay(0)
        self.User.setAutoRepeatInterval(0)
        self.User.setAutoDefault(False)
        self.User.setDefault(False)
        self.User.setFlat(True)
        self.User.setObjectName(_fromUtf8("User"))
        self.btn_Login = QtGui.QPushButton(self.Logar)
        self.btn_Login.setGeometry(QtCore.QRect(242, 336, 165, 48))
        self.btn_Login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Login.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_Login.setAutoFillBackground(False)
        self.btn_Login.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Login.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Login.setIcon(icon3)
        self.btn_Login.setIconSize(QtCore.QSize(163, 163))
        self.btn_Login.setFlat(True)
        self.btn_Login.setObjectName(_fromUtf8("btn_Login"))
        self.btn_Cadastro = QtGui.QPushButton(self.Logar)
        self.btn_Cadastro.setGeometry(QtCore.QRect(454, 338, 165, 48))
        self.btn_Cadastro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Cadastro.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_Cadastro.setAutoFillBackground(False)
        self.btn_Cadastro.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_cadastro.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Cadastro.setIcon(icon4)
        self.btn_Cadastro.setIconSize(QtCore.QSize(160, 160))
        self.btn_Cadastro.setFlat(True)
        self.btn_Cadastro.setObjectName(_fromUtf8("btn_Cadastro"))
        self.IconeSair = QtGui.QPushButton(self.Logar)
        self.IconeSair.setEnabled(True)
        self.IconeSair.setGeometry(QtCore.QRect(10, 14, 41, 39))
        self.IconeSair.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/Icone sair.png")), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/Icone sair.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.IconeSair.setIcon(icon5)
        self.IconeSair.setIconSize(QtCore.QSize(30, 30))
        self.IconeSair.setFlat(True)
        self.IconeSair.setObjectName(_fromUtf8("IconeSair"))
        self.Box_ExcluirCadastros = QtGui.QComboBox(self.Logar)
        self.Box_ExcluirCadastros.setGeometry(QtCore.QRect(366, 394, 113, 22))
        self.Box_ExcluirCadastros.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Box_ExcluirCadastros.setStyleSheet(_fromUtf8("color: rgb(153, 153, 153);\n"
"background-color: rgb(0, 22, 57);\n"
"text-decoration: underline;\n"
"font: 75 8pt \"Microsoft YaHei\";\n"
""))
        self.Box_ExcluirCadastros.setEditable(False)
        self.Box_ExcluirCadastros.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.Box_ExcluirCadastros.setDuplicatesEnabled(False)
        self.Box_ExcluirCadastros.setFrame(True)
        self.Box_ExcluirCadastros.setObjectName(_fromUtf8("Box_ExcluirCadastros"))
        self.Box_ExcluirCadastros.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.Logar)
        self.label.setGeometry(QtCore.QRect(312, 312, 239, 16))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Book Antiqua\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.SenhaMestre = QtGui.QLabel(self.Logar)
        self.SenhaMestre.setGeometry(QtCore.QRect(250, 432, 91, 21))
        self.SenhaMestre.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.SenhaMestre.setStyleSheet(_fromUtf8("color: rgb(153, 153, 153);\n"
"font: 75 10pt \"Microsoft YaHei\";"))
        self.SenhaMestre.setObjectName(_fromUtf8("SenhaMestre"))
        self.btn_Ir = QtGui.QPushButton(self.Logar)
        self.btn_Ir.setGeometry(QtCore.QRect(532, 428, 77, 33))
        self.btn_Ir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Ir.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Ir.setAutoFillBackground(False)
        self.btn_Ir.setStyleSheet(_fromUtf8("font: 11pt \"Century Gothic\";\n"
"color: rgb(0, 22, 57);\n"
"background-color: rgb(220, 20, 60);"))
        self.btn_Ir.setAutoDefault(False)
        self.btn_Ir.setObjectName(_fromUtf8("btn_Ir"))
        self.label_2 = QtGui.QLabel(self.Logar)
        self.label_2.setGeometry(QtCore.QRect(348, 470, 173, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Book Antiqua\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Login_Usuario = QtGui.QLineEdit(self.Logar)
        self.Login_Usuario.setGeometry(QtCore.QRect(242, 212, 375, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Login_Usuario.setFont(font)
        self.Login_Usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_Usuario.setObjectName(_fromUtf8("Login_Usuario"))
        self.Login_Senha = QtGui.QLineEdit(self.Logar)
        self.Login_Senha.setGeometry(QtCore.QRect(242, 268, 375, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Login_Senha.setFont(font)
        self.Login_Senha.setEchoMode(QtGui.QLineEdit.Password)
        self.Login_Senha.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_Senha.setObjectName(_fromUtf8("Login_Senha"))
        self.Login_SenhaMestre = QtGui.QLineEdit(self.Logar)
        self.Login_SenhaMestre.setGeometry(QtCore.QRect(344, 428, 185, 31))
        self.Login_SenhaMestre.setEchoMode(QtGui.QLineEdit.Password)
        self.Login_SenhaMestre.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_SenhaMestre.setObjectName(_fromUtf8("Login_SenhaMestre"))
        TelaLogin.setCentralWidget(self.Logar)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

    def retranslateUi(self, TelaLogin):
        TelaLogin.setWindowTitle(_translate("TelaLogin", "Logar", None))
        self.Box_ExcluirCadastros.setItemText(0, _translate("TelaLogin", "Excluir cadastros", None))
        self.label.setText(_translate("TelaLogin", "*Usuário e/ou senha incorretos*", None))
        self.SenhaMestre.setText(_translate("TelaLogin", "Senha mestre:", None))
        self.btn_Ir.setText(_translate("TelaLogin", "Ir", None))
        self.label_2.setText(_translate("TelaLogin", "*Senha mestre incorreta*", None))
        self.Login_Usuario.setPlaceholderText(_translate("TelaLogin", "Usuário", None))
        self.Login_Senha.setPlaceholderText(_translate("TelaLogin", "Senha", None))

