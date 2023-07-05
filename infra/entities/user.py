from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, UniqueConstraint


class User(Base):
    #Nome da tabela a ser criada
    __tablename__ = 'user'
    #Colunas da tabela que serão criadas na tabela
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    user = Column(String(100), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    access = Column(String(20), nullable=False)