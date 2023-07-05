from infra.configs.connection import DBConnectionHandler
from infra.entities.venda import Venda
from infra.entities.item_venda import ItemVenda
from sqlalchemy import func



class VendaRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Venda).all()
            return data



    def select_items(self, id_venda):
        with DBConnectionHandler() as db:
            venda = db.session.query(Venda).filter(Venda.numero == id_venda).first()
            itens = db.session.query(ItemVenda).filter(ItemVenda.id_venda == venda.id).all()
            return venda, itens

    def select_cliente(self, cliente):
        with DBConnectionHandler() as db:
            data = db.session.query(Venda).filter(Venda.cliente == cliente).first()
            return data

    def select_data(self, data1, data2):
        with DBConnectionHandler() as db:
            data = db.session.query(Venda).filter(Venda.data.between(data1, data2))
            return data

        #Métado para inserir usuario no banco de dados
    def insert(self, venda):
        with DBConnectionHandler() as db:
            try:
                db.session.add(venda)
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return e

    #Método para realizar a remoção de um usuario do banco de dados
    def delete(self, venda):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Venda).filter(Venda.id == venda).delete()
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return str(e)

    #Método para atualizar um usuario

    def update(self, venda):
        with DBConnectionHandler() as db:
            db.session.commit()
            try:
                db.session.query(Venda).filter(Venda.id == venda.id).update({Venda.numero: venda.numero, Venda.cliente: venda.cliente})
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return str(e)

    def get_max(self):
        with DBConnectionHandler() as db:
            data = db.session.query(func.max(Venda.id)).first()
        if len(data) > 0:
            return data[0]
        else:
            return 0
