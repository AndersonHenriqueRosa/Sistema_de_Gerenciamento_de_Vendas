# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sistema_venda.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 571)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.btn_pg_cadastro = QPushButton(self.centralwidget)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")

        self.gridLayout_7.addWidget(self.btn_pg_cadastro, 0, 1, 1, 1)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.pag_lista_vendas = QWidget()
        self.pag_lista_vendas.setObjectName(u"pag_lista_vendas")
        self.widget_5 = QWidget(self.pag_lista_vendas)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(70, 0, 649, 521))
        self.gridLayout_9 = QGridLayout(self.widget_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_2 = QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_7 = QFrame(self.widget_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.txt_data_inicial = QLineEdit(self.frame_6)
        self.txt_data_inicial.setObjectName(u"txt_data_inicial")

        self.horizontalLayout_11.addWidget(self.txt_data_inicial)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.txt_data_final = QLineEdit(self.frame_6)
        self.txt_data_final.setObjectName(u"txt_data_final")

        self.horizontalLayout_12.addWidget(self.txt_data_final)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        self.btn_filtrar_data = QPushButton(self.frame_6)
        self.btn_filtrar_data.setObjectName(u"btn_filtrar_data")

        self.horizontalLayout_13.addWidget(self.btn_filtrar_data)


        self.gridLayout_6.addWidget(self.frame_6, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.widget_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_8)
        self.formLayout.setObjectName(u"formLayout")
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_14.addWidget(self.label_14)

        self.txt_cliente = QLineEdit(self.frame_9)
        self.txt_cliente.setObjectName(u"txt_cliente")

        self.horizontalLayout_14.addWidget(self.txt_cliente)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)

        self.btn_filtrar_cliente = QPushButton(self.frame_9)
        self.btn_filtrar_cliente.setObjectName(u"btn_filtrar_cliente")

        self.horizontalLayout_15.addWidget(self.btn_filtrar_cliente)


        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.widget_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_28.addWidget(self.label_15)

        self.btn_consultar_tudo = QPushButton(self.frame_10)
        self.btn_consultar_tudo.setObjectName(u"btn_consultar_tudo")

        self.horizontalLayout_28.addWidget(self.btn_consultar_tudo)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.gridLayout_9.addWidget(self.widget_7, 1, 0, 1, 2)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_14 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_14)

        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_18.addWidget(self.label_9)

        self.horizontalSpacer_15 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_15)


        self.gridLayout_9.addWidget(self.widget_6, 0, 0, 1, 2)

        self.frame_5 = QFrame(self.widget_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tw_vendas = QTableWidget(self.frame_5)
        if (self.tw_vendas.columnCount() < 4):
            self.tw_vendas.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_vendas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_vendas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_vendas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_vendas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tw_vendas.setObjectName(u"tw_vendas")

        self.verticalLayout_3.addWidget(self.tw_vendas)

        self.widget_8 = QWidget(self.frame_5)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_11 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)

        self.btn_pg_venda = QPushButton(self.widget_8)
        self.btn_pg_venda.setObjectName(u"btn_pg_venda")

        self.horizontalLayout_17.addWidget(self.btn_pg_venda)

        self.horizontalSpacer_13 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_13)


        self.verticalLayout_3.addWidget(self.widget_8)


        self.gridLayout_9.addWidget(self.frame_5, 2, 0, 1, 2)

        self.Pages.addWidget(self.pag_lista_vendas)
        self.pag_venda = QWidget()
        self.pag_venda.setObjectName(u"pag_venda")
        self.gridLayout_5 = QGridLayout(self.pag_venda)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_3 = QWidget(self.pag_venda)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(295, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(249, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addWidget(self.widget)

        self.widget_12 = QWidget(self.widget_3)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_3 = QGridLayout(self.widget_12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout = QGridLayout(self.widget_15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_15)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txt_iv_numero = QLineEdit(self.widget_15)
        self.txt_iv_numero.setObjectName(u"txt_iv_numero")

        self.horizontalLayout.addWidget(self.txt_iv_numero)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(227, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_15)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.txt_iv_cliente = QLineEdit(self.widget_15)
        self.txt_iv_cliente.setObjectName(u"txt_iv_cliente")

        self.horizontalLayout_3.addWidget(self.txt_iv_cliente)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_15)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.txt_iv_data = QLineEdit(self.widget_15)
        self.txt_iv_data.setObjectName(u"txt_iv_data")

        self.horizontalLayout_2.addWidget(self.txt_iv_data)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_15, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_2 = QGridLayout(self.widget_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.cb_iv_descricao = QComboBox(self.widget_14)
        self.cb_iv_descricao.addItem("")
        self.cb_iv_descricao.addItem("")
        self.cb_iv_descricao.addItem("")
        self.cb_iv_descricao.addItem("")
        self.cb_iv_descricao.addItem("")
        self.cb_iv_descricao.setObjectName(u"cb_iv_descricao")

        self.horizontalLayout_4.addWidget(self.cb_iv_descricao)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.widget_14)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.txt_iv_preco = QLineEdit(self.widget_14)
        self.txt_iv_preco.setObjectName(u"txt_iv_preco")

        self.horizontalLayout_5.addWidget(self.txt_iv_preco)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(227, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.widget_14)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.txt_iv_qtd = QLineEdit(self.widget_14)
        self.txt_iv_qtd.setObjectName(u"txt_iv_qtd")

        self.horizontalLayout_6.addWidget(self.txt_iv_qtd)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_14, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_12)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout = QVBoxLayout(self.widget_11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_item_venda = QTableWidget(self.widget_11)
        if (self.tw_item_venda.columnCount() < 3):
            self.tw_item_venda.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_item_venda.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_item_venda.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_item_venda.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tw_item_venda.setObjectName(u"tw_item_venda")
        self.tw_item_venda.setSortingEnabled(False)
        self.tw_item_venda.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout.addWidget(self.tw_item_venda)

        self.widget_4 = QWidget(self.widget_11)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(283, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.btn_concluir_venda = QPushButton(self.widget_4)
        self.btn_concluir_venda.setObjectName(u"btn_concluir_venda")

        self.horizontalLayout_8.addWidget(self.btn_concluir_venda)

        self.horizontalSpacer_10 = QSpacerItem(282, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addWidget(self.widget_4)


        self.verticalLayout_5.addWidget(self.widget_11)


        self.gridLayout_5.addWidget(self.widget_3, 0, 0, 1, 1)

        self.Pages.addWidget(self.pag_venda)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_4 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_20 = QLabel(self.pg_cadastro)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_20)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_21 = QLabel(self.pg_cadastro)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_16.addWidget(self.label_21)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")

        self.horizontalLayout_16.addWidget(self.txt_nome)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_22 = QLabel(self.pg_cadastro)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_23.addWidget(self.label_22)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")

        self.horizontalLayout_23.addWidget(self.txt_usuario)


        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_23 = QLabel(self.pg_cadastro)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_24.addWidget(self.label_23)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")

        self.horizontalLayout_24.addWidget(self.txt_senha)


        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_24 = QLabel(self.pg_cadastro)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_25.addWidget(self.label_24)

        self.txt_senha2 = QLineEdit(self.pg_cadastro)
        self.txt_senha2.setObjectName(u"txt_senha2")

        self.horizontalLayout_25.addWidget(self.txt_senha2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_25 = QLabel(self.pg_cadastro)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_26.addWidget(self.label_25)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")

        self.horizontalLayout_26.addWidget(self.cb_perfil)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_26 = QLabel(self.pg_cadastro)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_27.addWidget(self.label_26)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.horizontalLayout_27.addWidget(self.btn_cadastrar)

        self.btn_cadastro_concluir = QPushButton(self.pg_cadastro)
        self.btn_cadastro_concluir.setObjectName(u"btn_cadastro_concluir")

        self.horizontalLayout_27.addWidget(self.btn_cadastro_concluir)

        self.label_27 = QLabel(self.pg_cadastro)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_27.addWidget(self.label_27)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.Pages.addWidget(self.pg_cadastro)

        self.gridLayout_7.addWidget(self.Pages, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Filtrar por data</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Data inicial</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Data final</span></p></body></html>", None))
        self.btn_filtrar_data.setText(QCoreApplication.translate("MainWindow", u"pesquisar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Filtrar por Cliente</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Cliente</span></p></body></html>", None))
        self.btn_filtrar_cliente.setText(QCoreApplication.translate("MainWindow", u"pesquisar", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Consultar </span></p></body></html>", None))
        self.btn_consultar_tudo.setText(QCoreApplication.translate("MainWindow", u"pesquisar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Vendas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tw_vendas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem1 = self.tw_vendas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem2 = self.tw_vendas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem3 = self.tw_vendas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total da venda", None));
        self.btn_pg_venda.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Item de Venda</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Numero</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Descri\u00e7\u00e3o</span></p></body></html>", None))
        self.cb_iv_descricao.setItemText(0, "")
        self.cb_iv_descricao.setItemText(1, QCoreApplication.translate("MainWindow", u"MDF Farm Nuances 6mm 2 Faces Arauco", None))
        self.cb_iv_descricao.setItemText(2, QCoreApplication.translate("MainWindow", u"MDF Damasco Matt 18mm 2 Faces Arauco", None))
        self.cb_iv_descricao.setItemText(3, QCoreApplication.translate("MainWindow", u"MDF S\u00e1lvia Matt 6mm 2 Faces Arauco", None))
        self.cb_iv_descricao.setItemText(4, QCoreApplication.translate("MainWindow", u"MDF Verde Mar 18mm 2 Faces 185cm x 275cm Eucatex", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Pre\u00e7o</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Qtd</span></p></body></html>", None))
        ___qtablewidgetitem4 = self.tw_item_venda.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tw_item_venda.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem6 = self.tw_item_venda.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Qtd", None));
        self.btn_concluir_venda.setText(QCoreApplication.translate("MainWindow", u"Concluir", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Confirma senha:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Perfil:</p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_26.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_cadastro_concluir.setText(QCoreApplication.translate("MainWindow", u"Concluir", None))
        self.label_27.setText("")
    # retranslateUi

