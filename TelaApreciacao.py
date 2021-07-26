# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaApreciacao.ui'
#
# Created: Thu May 30 00:03:17 2019
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

class Ui_TelaApreciar(object):
    def setupUi(self, TelaApreciar):
        TelaApreciar.setObjectName(_fromUtf8("TelaApreciar"))
        TelaApreciar.resize(850, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaApreciar.sizePolicy().hasHeightForWidth())
        TelaApreciar.setSizePolicy(sizePolicy)
        TelaApreciar.setMinimumSize(QtCore.QSize(850, 500))
        TelaApreciar.setMaximumSize(QtCore.QSize(850, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/icone.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        TelaApreciar.setWindowIcon(icon)
        TelaApreciar.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 28, 72);"))
        TelaApreciar.setTabShape(QtGui.QTabWidget.Rounded)
        self.Apreciacao = QtGui.QWidget(TelaApreciar)
        self.Apreciacao.setObjectName(_fromUtf8("Apreciacao"))
        self.PlanodeFundo = QtGui.QPushButton(self.Apreciacao)
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
        self.treeWidget_Vencer = QtGui.QTreeWidget(self.Apreciacao)
        self.treeWidget_Vencer.setGeometry(QtCore.QRect(46, 64, 765, 173))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_Vencer.sizePolicy().hasHeightForWidth())
        self.treeWidget_Vencer.setSizePolicy(sizePolicy)
        self.treeWidget_Vencer.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"
"color: rgb(0, 22, 57);\n"
"background-color: rgb(255, 255, 255);"))
        self.treeWidget_Vencer.setFrameShape(QtGui.QFrame.Box)
        self.treeWidget_Vencer.setFrameShadow(QtGui.QFrame.Raised)
        self.treeWidget_Vencer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_Vencer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeWidget_Vencer.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeWidget_Vencer.setUniformRowHeights(True)
        self.treeWidget_Vencer.setItemsExpandable(False)
        self.treeWidget_Vencer.setAnimated(True)
        self.treeWidget_Vencer.setObjectName(_fromUtf8("treeWidget_Vencer"))
        self.treeWidget_Vencer.header().setVisible(True)
        self.treeWidget_Vencer.header().setCascadingSectionResizes(True)
        self.treeWidget_Vencer.header().setDefaultSectionSize(186)
        self.treeWidget_Vencer.header().setHighlightSections(True)
        self.treeWidget_Vencer.header().setMinimumSectionSize(50)
        self.treeWidget_Vencer.header().setSortIndicatorShown(False)
        self.treeWidget_Vencer.header().setStretchLastSection(False)
        self.btn_Voltar_2 = QtGui.QPushButton(self.Apreciacao)
        self.btn_Voltar_2.setGeometry(QtCore.QRect(24, 14, 53, 33))
        self.btn_Voltar_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Imagens/btn_Voltar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Voltar_2.setIcon(icon2)
        self.btn_Voltar_2.setIconSize(QtCore.QSize(40, 40))
        self.btn_Voltar_2.setFlat(True)
        self.btn_Voltar_2.setObjectName(_fromUtf8("btn_Voltar_2"))
        self.treeWidget_Vencidos = QtGui.QTreeWidget(self.Apreciacao)
        self.treeWidget_Vencidos.setGeometry(QtCore.QRect(46, 292, 765, 169))
        self.treeWidget_Vencidos.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.treeWidget_Vencidos.setFrameShape(QtGui.QFrame.Box)
        self.treeWidget_Vencidos.setFrameShadow(QtGui.QFrame.Raised)
        self.treeWidget_Vencidos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget_Vencidos.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeWidget_Vencidos.setRootIsDecorated(True)
        self.treeWidget_Vencidos.setUniformRowHeights(True)
        self.treeWidget_Vencidos.setItemsExpandable(False)
        self.treeWidget_Vencidos.setAnimated(True)
        self.treeWidget_Vencidos.setObjectName(_fromUtf8("treeWidget_Vencidos"))
        self.treeWidget_Vencidos.header().setVisible(True)
        self.treeWidget_Vencidos.header().setCascadingSectionResizes(True)
        self.treeWidget_Vencidos.header().setDefaultSectionSize(289)
        self.treeWidget_Vencidos.header().setHighlightSections(False)
        self.treeWidget_Vencidos.header().setMinimumSectionSize(50)
        self.treeWidget_Vencidos.header().setStretchLastSection(False)
        self.produtosvencidos = QtGui.QLabel(self.Apreciacao)
        self.produtosvencidos.setGeometry(QtCore.QRect(286, 244, 283, 39))
        self.produtosvencidos.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.produtosvencidos.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 22, 57);\n"
"font: 87 25pt \"Exo\";"))
        self.produtosvencidos.setFrameShape(QtGui.QFrame.NoFrame)
        self.produtosvencidos.setFrameShadow(QtGui.QFrame.Plain)
        self.produtosvencidos.setTextFormat(QtCore.Qt.AutoText)
        self.produtosvencidos.setObjectName(_fromUtf8("produtosvencidos"))
        self.produtosparasevencer = QtGui.QLabel(self.Apreciacao)
        self.produtosparasevencer.setGeometry(QtCore.QRect(242, 12, 371, 39))
        self.produtosparasevencer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.produtosparasevencer.setAutoFillBackground(False)
        self.produtosparasevencer.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 22, 57);\n"
"font: 87 25pt \"Exo\";"))
        self.produtosparasevencer.setOpenExternalLinks(False)
        self.produtosparasevencer.setObjectName(_fromUtf8("produtosparasevencer"))
        self.nenhumprodutovencido = QtGui.QLabel(self.Apreciacao)
        self.nenhumprodutovencido.setGeometry(QtCore.QRect(160, 140, 531, 39))
        self.nenhumprodutovencido.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.nenhumprodutovencido.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 22, 57);\n"
"font: 87 25pt \"Exo\";"))
        self.nenhumprodutovencido.setFrameShape(QtGui.QFrame.NoFrame)
        self.nenhumprodutovencido.setFrameShadow(QtGui.QFrame.Plain)
        self.nenhumprodutovencido.setText(_fromUtf8(""))
        self.nenhumprodutovencido.setTextFormat(QtCore.Qt.AutoText)
        self.nenhumprodutovencido.setObjectName(_fromUtf8("nenhumprodutovencido"))
        self.nenhumprodutovencido_2 = QtGui.QLabel(self.Apreciacao)
        self.nenhumprodutovencido_2.setGeometry(QtCore.QRect(230, 370, 385, 39))
        self.nenhumprodutovencido_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.nenhumprodutovencido_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 22, 57);\n"
"font: 87 25pt \"Exo\";"))
        self.nenhumprodutovencido_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.nenhumprodutovencido_2.setFrameShadow(QtGui.QFrame.Plain)
        self.nenhumprodutovencido_2.setText(_fromUtf8(""))
        self.nenhumprodutovencido_2.setTextFormat(QtCore.Qt.AutoText)
        self.nenhumprodutovencido_2.setObjectName(_fromUtf8("nenhumprodutovencido_2"))
        TelaApreciar.setCentralWidget(self.Apreciacao)

        self.retranslateUi(TelaApreciar)
        QtCore.QMetaObject.connectSlotsByName(TelaApreciar)

    def retranslateUi(self, TelaApreciar):
        TelaApreciar.setWindowTitle(_translate("TelaApreciar", "Apreciar ", None))
        self.treeWidget_Vencer.headerItem().setText(0, _translate("TelaApreciar", "Produto", None))
        self.treeWidget_Vencer.headerItem().setText(1, _translate("TelaApreciar", "Lote", None))
        self.treeWidget_Vencer.headerItem().setText(2, _translate("TelaApreciar", "Validade", None))
        self.treeWidget_Vencer.headerItem().setText(3, _translate("TelaApreciar", "Dias Restantes", None))
        self.treeWidget_Vencidos.headerItem().setText(0, _translate("TelaApreciar", "Produto", None))
        self.treeWidget_Vencidos.headerItem().setText(1, _translate("TelaApreciar", "Lote", None))
        self.treeWidget_Vencidos.headerItem().setText(2, _translate("TelaApreciar", "Validade", None))
        self.produtosvencidos.setToolTip(_translate("TelaApreciar", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.produtosvencidos.setWhatsThis(_translate("TelaApreciar", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.produtosvencidos.setText(_translate("TelaApreciar", "Produtos vencidos", None))
        self.produtosparasevencer.setToolTip(_translate("TelaApreciar", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.produtosparasevencer.setWhatsThis(_translate("TelaApreciar", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.produtosparasevencer.setText(_translate("TelaApreciar", "Produtos para se vencer", None))
        self.nenhumprodutovencido.setToolTip(_translate("TelaApreciar", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.nenhumprodutovencido.setWhatsThis(_translate("TelaApreciar", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.nenhumprodutovencido_2.setToolTip(_translate("TelaApreciar", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.nenhumprodutovencido_2.setWhatsThis(_translate("TelaApreciar", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))

