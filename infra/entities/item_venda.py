from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DECIMAL


class ItemVenda(Base):
    #Nome da tabela a ser criada
    __tablename__ = 'itemVenda'
    #Colunas da tabela que serão criadas na tabela
    id = Column(Integer, autoincrement=True, primary_key=True)
    descricao = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(DECIMAL, nullable=False)
    id_venda = Column(Integer, ForeignKey('venda.id'))
