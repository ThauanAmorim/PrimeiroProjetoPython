# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaExcluirLogin.ui'
#
# Created: Wed May 29 02:46:48 2019
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

class Ui_TelaUsuarios(object):
    def setupUi(self, TelaUsuarios):
        TelaUsuarios.setObjectName(_fromUtf8("TelaUsuarios"))
        TelaUsuarios.resize(850, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaUsuarios.sizePolicy().hasHeightForWidth())
        TelaUsuarios.setSizePolicy(sizePolicy)
        TelaUsuarios.setMinimumSize(QtCore.QSize(850, 500))
        TelaUsuarios.setMaximumSize(QtCore.QSize(850, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/icone.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        TelaUsuarios.setWindowIcon(icon)
        TelaUsuarios.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 28, 72);"))
        TelaUsuarios.setTabShape(QtGui.QTabWidget.Rounded)
        self.Users = QtGui.QWidget(TelaUsuarios)
        self.Users.setObjectName(_fromUtf8("Users"))
        self.PlanodeFundo = QtGui.QPushButton(self.Users)
        self.PlanodeFundo.setGeometry(QtCore.QRect(-10, -4, 871, 525))
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
        self.treeWidget_Users = QtGui.QTreeWidget(self.Users)
        self.treeWidget_Users.setGeometry(QtCore.QRect(50, 126, 765, 227))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_Users.sizePolicy().hasHeightForWidth())
        self.treeWidget_Users.setSizePolicy(sizePolicy)
        self.treeWidget_Users.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"
"color: rgb(0, 22, 57);\n"
"background-color: rgb(255, 255, 255);"))
        self.treeWidget_Users.setFrameShape(QtGui.QFrame.Box)
        self.treeWidget_Users.setFrameShadow(QtGui.QFrame.Raised)
        self.treeWidget_Users.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_Users.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget_Users.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeWidget_Users.setUniformRowHeights(True)
        self.treeWidget_Users.setItemsExpandable(False)
        self.treeWidget_Users.setAnimated(True)
        self.treeWidget_Users.setObjectName(_fromUtf8("treeWidget_Users"))
        self.treeWidget_Users.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget_Users.headerItem().setForeground(0, brush)
        self.treeWidget_Users.header().setVisible(True)
        self.treeWidget_Users.header().setCascadingSectionResizes(True)
        self.treeWidget_Users.header().setDefaultSectionSize(186)
        self.treeWidget_Users.header().setHighlightSections(True)
        self.treeWidget_Users.header().setMinimumSectionSize(50)
        self.treeWidget_Users.header().setSortIndicatorShown(False)
        self.treeWidget_Users.header().setStretchLastSection(False)
        self.btn_Voltar_2 = QtGui.QPushButton(self.Users)
        self.btn_Voltar_2.setGeometry(QtCore.QRect(24, 26, 53, 33))
        self.btn_Voltar_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Voltar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Voltar_2.setIcon(icon2)
        self.btn_Voltar_2.setIconSize(QtCore.QSize(40, 40))
        self.btn_Voltar_2.setFlat(True)
        self.btn_Voltar_2.setObjectName(_fromUtf8("btn_Voltar_2"))
        self.usuarios = QtGui.QLabel(self.Users)
        self.usuarios.setGeometry(QtCore.QRect(364, 64, 139, 39))
        self.usuarios.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.usuarios.setAutoFillBackground(False)
        self.usuarios.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 22, 57);\n"
"font: 87 25pt \"Exo\";"))
        self.usuarios.setOpenExternalLinks(False)
        self.usuarios.setObjectName(_fromUtf8("usuarios"))
        self.btn_Apagar = QtGui.QPushButton(self.Users)
        self.btn_Apagar.setGeometry(QtCore.QRect(314, 380, 227, 55))
        self.btn_Apagar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Apagar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_Apagar.setAutoFillBackground(False)
        self.btn_Apagar.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Apagar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Apagar.setIcon(icon3)
        self.btn_Apagar.setIconSize(QtCore.QSize(210, 210))
        self.btn_Apagar.setFlat(True)
        self.btn_Apagar.setObjectName(_fromUtf8("btn_Apagar"))
        self.semUsuarios = QtGui.QLabel(self.Users)
        self.semUsuarios.setGeometry(QtCore.QRect(200, 224, 455, 51))
        self.semUsuarios.setAcceptDrops(False)
        self.semUsuarios.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.semUsuarios.setAutoFillBackground(False)
        self.semUsuarios.setStyleSheet(_fromUtf8("\n"
"color: rgb(255, 0, 0);\n"
"font: 22pt \"Bahnschrift\";"))
        self.semUsuarios.setFrameShape(QtGui.QFrame.NoFrame)
        self.semUsuarios.setFrameShadow(QtGui.QFrame.Sunken)
        self.semUsuarios.setText(_fromUtf8(""))
        self.semUsuarios.setTextFormat(QtCore.Qt.RichText)
        self.semUsuarios.setObjectName(_fromUtf8("semUsuarios"))
        TelaUsuarios.setCentralWidget(self.Users)

        self.retranslateUi(TelaUsuarios)
        QtCore.QMetaObject.connectSlotsByName(TelaUsuarios)

    def retranslateUi(self, TelaUsuarios):
        TelaUsuarios.setWindowTitle(_translate("TelaUsuarios", "Users", None))
        self.treeWidget_Users.headerItem().setText(0, _translate("TelaUsuarios", "Usuários", None))
        self.usuarios.setToolTip(_translate("TelaUsuarios", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.usuarios.setWhatsThis(_translate("TelaUsuarios", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.usuarios.setText(_translate("TelaUsuarios", "Usuários", None))

