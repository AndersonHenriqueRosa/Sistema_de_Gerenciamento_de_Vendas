import datetime

from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey


class Venda(Base):
    #Nome da tabela a ser criada
    __tablename__ = 'venda'
    #Colunas da tabela que serão criadas na tabela
    id = Column(Integer, autoincrement=True, primary_key=True)
    numero = Column(Integer, nullable=False)
    cliente = Column(String(100), nullable=False, unique=True)
    data = Column(DateTime(), default=datetime.datetime.now())
    data_atualizado = Column(DateTime(), default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    #usuario = Column(Integer, ForeignKey("user.id"))
