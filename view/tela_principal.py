from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QComboBox, QLabel, QLineEdit, QTableWidget,QAbstractItemView, QTableWidgetItem,
                               QWidget, QPushButton, QMessageBox, QSizePolicy)

from ui_login import Ui_Login
from ui_sistema_venda import Ui_MainWindow
import sys

from infra.entities.user import User
from infra.entities.venda import Venda
from infra.entities.item_venda import ItemVenda
from infra.repository.user_repository import UserRepository
from infra.repository.venda_repository import VendaRepository
from infra.repository.item_venda_repository import ItemVendaRepository


from infra.configs.connection import DBConnectionHandler

# class Login(QWidget, Ui_Login):
#     def __init__(self) -> None:
#         super(Login, self).__init__()
#         self.tentativas = 0
#         self.setupUi(self)
#         self.setWindowTitle("Login do Sistema")

        #self.btn_login.clicked.connect(self.checkLogin)
        #self.btn_login.clicked.connect(self.open_system)


    # def open_system(self):
    #     if self.txt_password.text() == '1234':
    #         autenticado = "administrador"
    #         if autenticado.lower() == "administrador" or autenticado.lower() == "usuario":
    #             self.w = MainWindow(autenticado.lower())
    #             self.w.show()
    #             self.close()
    #         else:
    #
    #             if self.tentativas < 3:
    #                 msm = QMessageBox()
    #                 msm.setIcon(QMessageBox.Warning)
    #                 msm.setWindowTitle("Erro ao acessar")
    #                 msm.setText(f'Login ou Senha incorreto \n \n Tentativa: {self.tentativas + 1} de 3')
    #                 msm.exec()
    #                 self.tentativas += 1
    #             if self.tentativas == 3:
    #                 DBConnectionHandler.__exit__()
    #                 sys.exit(0)
    #
    #     else:
    #         print('Senha invàlida')
    #
    # def checkLogin(self):
    #     db = UserRepository()
    #     user = self.txt_user.text().upper()
    #     password = self.txt_password.text()
    #     autenticado = db.check_user(user, password)
    #
    #     if autenticado.lower() == "administrador" or autenticado.lower() == "usuario":
    #         self.w = MainWindow(autenticado.lower())
    #         self.w.show()
    #         self.close()
    #     else:
    #
    #         if self.tentativas < 3:
    #             msm = QMessageBox()
    #             msm.setIcon(QMessageBox.Warning)
    #             msm.setWindowTitle("Erro ao acessar")
    #             msm.setText(f'Login ou Senha incorreto \n \n Tentativa: {self.tentativas +1} de 3')
    #             msm.exec()
    #             self.tentativas += 1
    #         if self.tentativas == 3:
    #             DBConnectionHandler.__exit__()
    #             sys.exit(0)




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento de venda")

        # if user.lower() == "usuario":
        #     self.btn_pg_cadastro.setVisible(False)

        self.btn_pg_cadastro.clicked.connect(lambda : self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_cadastrar.clicked.connect(self.cadastrar_user)
        #self.btn_cadastro_concluir.clicked.connect(self.adicionar_venda)
        #self.btn_cadastro_concluir.clicked.connect(self.cadastrar_item_venda)

        self.btn_cadastro_concluir.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pag_lista_vendas))
        self.btn_concluir_venda.clicked.connect(self.adicionar_venda)
        #self.btn_concluir_venda.clicked.connect(self.cadastrar_item_venda)
        self.btn_concluir_venda.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pag_lista_vendas))
        self.btn_pg_venda.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pag_venda))
        self.btn_pg_venda.clicked.connect(self.carrega_numero)
        self.tw_item_venda.cellDoubleClicked.connect(self.carrega_dados_item_venda)
        self.tw_vendas.cellDoubleClicked.connect(self.popula_tabela_item_venda)
        self.tw_vendas.cellDoubleClicked.connect(lambda: self.Pages.setCurrentWidget(self.pag_venda))
        self.tw_vendas.cellDoubleClicked.connect(self.carrega_dados_venda)
        self.popula_tabela_venda()

    def cadastrar_user(self):

        if self.txt_senha.text() != self.txt_senha2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Senhas divergentes')
            msg.setText('A senha não é igual!')
            msg.exec()
            return None

        db = UserRepository()

        user = User(
        name=self.txt_nome.text(),
        user=self.txt_usuario.text(),
        password=self.txt_senha.text(),
        access=self.cb_perfil.currentText()
        )

        if self.btn_cadastrar.text() == 'Cadastrar':
            retorno = db.insert(user)

            if retorno == 'OK':
                msg = QMessageBox()
                msg.setWindowTitle('Cadastro realizado')
                msg.setText('Cadastro realizado com sucesso.')
                msg.exec()
                #self.limpar_campos()
            elif retorno == 'UNIQUE constraint failed: USER.USER':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.critical)
                msg.setWindowTitle('Usuário já cadastrado')
                msg.setText(f'O usuário {self.txt_usuario.text()} já está sendo usado')
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.critical)
                msg.setWindowTitle('Erro ao cadastrar')
                msg.setText('Erro ao cadastrar o usuário, verifique os dados inserido')
                msg.exec()
        elif self.btn_cadastrar.text() == 'Atualizar':
            retorno = db.update(user)
            if retorno == 'OK':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.information)
                msg.setWindowTitle('Cadastro atualizado')
                msg.setText('Cadastro atualizado com sucesso.')
                msg.exec()
                #self.limpar_campos()
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Erro ao atualizar')
                msg.setText('Erro ao atualizar o usuário, verifique os dados inserido')
                msg.exec()

    def adicionar_venda(self):
        db = VendaRepository()
        venda = Venda(
        numero=self.txt_iv_numero.text(),
        cliente=self.txt_iv_cliente.text()
        )

        if self.btn_concluir_venda.text() == 'Concluir':
            retorno = db.insert(venda)

            if retorno == 'OK':
                msg = QMessageBox()
                msg.setWindowTitle('Venda adicionado')
                msg.setText('Venda adicionado com sucesso.')
                msg.exec()
                #self.limpar_campos()
        self.cadastrar_item_venda()
        self.popula_tabela_venda()
        self.popula_tabela_item_venda()

    def cadastrar_item_venda(self):
        db = ItemVendaRepository()

        itemVenda = ItemVenda(
            descricao=self.cb_iv_descricao.currentText(),
            quantidade=self.txt_iv_qtd.text(),
            preco=self.txt_iv_preco.text(),
            id_venda = self.txt_iv_numero.text()
        )

        if self.btn_concluir_venda.text() == 'Concluir':
            retorno = db.insert(itemVenda)

            if retorno == 'OK':
                msg = QMessageBox()
                msg.setWindowTitle('Item adicionado')
                msg.setText('Item adicionado com sucesso.')
                msg.exec()
                #self.limpar_campos()
            elif retorno == 'UNIQUE constraint failed: ITEMVENDA.ITEMVENDA':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.critical)
                msg.setWindowTitle('item já adicionado')
                msg.setText(f'O item {self.cb_iv_descricao.currentText()} já está sendo usado')
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao adicionar')
                msg.setText('Erro ao adicionar o item, verifique os dados inserido')
                msg.exec()
        elif self.btn_concluir_venda.text() == 'Atualizar':
            retorno = db.update(itemVenda)
            if retorno == 'OK':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.information)
                msg.setWindowTitle('Item atualizado')
                msg.setText('Item atualizado com sucesso.')
                msg.exec()
                #self.limpar_campos()
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Erro ao atualizar')
                msg.setText('Erro ao atualizar o item, verifique os dados inserido')
                msg.exec()
        self.popula_tabela_item_venda()

    def carrega_numero(self):
        db_venda = VendaRepository()
        id_ultima_venda = db_venda.get_max()
        id_ultima_venda += 1
        self.txt_iv_numero.setText(str(id_ultima_venda))
        self.txt_iv_numero.setReadOnly(True)


    def consulta_item_venda(self):
        if self.cb_iv_descricao.currentText() != '':
            db = ItemVendaRepository
            retorno = db.select(self.cb_iv_descricao.currentText())

            if retorno is not None:
                self.btn_concluir_venda.setText('Atualizar')
                msg = QMessageBox()
                msg.setWindowTitle('Item já adicionado')
                msg.setText(f'O item {self.cb_iv_descricao.currentText()} já esta adicionado')
                msg.exec()
                descr_map = {'MDF Farm Nuances 6mm 2 Faces Arauco': 1, 'MDF Damasco Matt 18mm 2 Faces Arauco': 2,
                             'MDF Sálvia Matt 6mm 2 Faces Arauco': 3,
                             'MDF Verde Mar 18mm 2 Faces 185cm x 275cm Eucatex': 4}
                self.cb_iv_descricao.setCurrentIndex((descr_map.get(retorno[0], 0)))
                self.txt_iv_preco.setText(retorno[1])
                self.txt_iv_qtd.setText(retorno[2])
                #self.btn_exluir_item_venda.setVisible(True)
                #self.txt_iv_numero.setReadOnly(True)
                #self.txt_iv_data.setReadOnly(True)
                #self.txt_iv_cliente.setReadOnly(True)
                #self.cb_iv_descricao.setReadOnly(True)
                #self.txt_iv_preco.setReadOnly(True)

    def popula_tabela_venda(self):
        self.tw_vendas.setRowCount(0)
        db = VendaRepository()
        lista_vendas = db.select_all()
        self.tw_vendas.setRowCount(len(lista_vendas))

        linha = 0

        for venda in lista_vendas:
            valores = [venda.numero, venda.cliente, venda.data]
            for valor in valores:
                item = QTableWidgetItem(str(valor))
                self.tw_vendas.setItem(linha, valores.index(valor), item)
                self.tw_vendas.item(linha, valores.index(valor))
            linha += 1

    def popula_tabela_item_venda(self, item):

        column_index = 0  # Índice da primeira coluna (começando em 0)
        column_value = self.tw_vendas.item(item, column_index).text()
        db = VendaRepository()
        lista_item_vendas = db.select_items(column_value)

        linha = 0
        self.tw_item_venda.setRowCount(len(lista_item_vendas[1]))
        for itemvenda in lista_item_vendas[1]:
            valores = [itemvenda.descricao, itemvenda.quantidade, itemvenda.preco]
            for coluna, valor in enumerate(valores):
                item = QTableWidgetItem(str(valor))
                self.tw_item_venda.setItem(linha, coluna, item)
            linha += 1

    def limpar_campos(self):
        for widget in self.container.children():
            if isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)

    def carrega_dados_venda(self, row, column):
        self.txt_iv_numero.setText(
            self.tw_vendas.item(row, 0).text() if self.tw_vendas.item(row, 0) is not None else "")
        self.txt_iv_cliente.setText(
            self.tw_vendas.item(row, 1).text() if self.tw_vendas.item(row, 1) is not None else "")
        self.txt_iv_data.setText(
            self.tw_item_venda.item(row, 2).text() if self.tw_item_venda.item(row, 2) is not None else "")


    def carrega_dados_item_venda(self, row, column):
        descr_map = {'MDF Farm Nuances 6mm 2 Faces Arauco': 1, 'MDF Damasco Matt 18mm 2 Faces Arauco': 2,
                     'MDF Sálvia Matt 6mm 2 Faces Arauco': 3,
                     'MDF Verde Mar 18mm 2 Faces 185cm x 275cm Eucatex': 4}
        self.cb_iv_descricao.setCurrentIndex(
            descr_map.get(self.tw_item_venda.item(row, 0).text(), 0) if self.tw_item_venda.item(row, 0) is not None else 0)
        self.txt_iv_preco.setText(
            self.tw_item_venda.item(row, 1).text() if self.tw_item_venda.item(row, 1) is not None else "")
        self.txt_iv_qtd.setText(
            self.tw_item_venda.item(row, 2).text() if self.tw_item_venda.item(row, 2) is not None else "")

        self.btn_concluir_venda.setText('Atualizar')
        #self.btn_exluir_item_venda.setVisible(True)
        #self.txt_iv_numero.setReadOnly(True)
        #self.txt_iv_data.setReadOnly(True)
        #self.txt_iv_cliente.setReadOnly(True)
        #self.cb_iv_descricao.setReadOnly(True)
        #self.txt_iv_preco.setReadOnly(True)
