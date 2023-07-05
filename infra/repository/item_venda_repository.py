from infra.configs.connection import DBConnectionHandler
from infra.entities.item_venda import ItemVenda
from infra.repository.venda_repository import VendaRepository

from sqlalchemy import CursorResult

class ItemVendaRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(ItemVenda).all()
            return data



    def select(self, descricao):
        with DBConnectionHandler() as db:
            data = db.session.query(ItemVenda).filter(ItemVenda.descricao == descricao).first()
            return data


        #Métado para inserir usuario no banco de dados
    def insert(self, itemVenda):
        with DBConnectionHandler() as db:
            try:
                db.session.add(itemVenda)
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return e

    #Método para realizar a remoção de um usuario do banco de dados
    def delete(self,itemVenda):
        with DBConnectionHandler() as db:
            try:
                db.session.query(ItemVenda).filter(ItemVenda.id == itemVenda).delete()
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return str(e)

    #Método para atualizar um usuario

    def update(self, itemVenda):

        with DBConnectionHandler() as db:
            db.session.commit()
            try:
                db.session.query(ItemVenda).filter(ItemVenda.descricao == itemVenda.descricao).update({ItemVenda.quantidade: itemVenda.quantidade, ItemVenda.preco: itemVenda.preco})
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return str(e)
