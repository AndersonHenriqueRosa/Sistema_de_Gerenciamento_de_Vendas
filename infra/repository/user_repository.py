from infra.configs.connection import DBConnectionHandler
from infra.entities.user import User


class UserRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(User).all()
            return data

    def select(self, name):
        with DBConnectionHandler() as db:
            data = db.session.query(User).filter(User.name == name).first()
            return data


        #Métado para inserir usuario no banco de dados
    def insert(self, user):
        with DBConnectionHandler() as db:
            try:
                db.session.add(user)
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return e

    def check_user(self, user, password):
        with DBConnectionHandler() as db:
            try:
                resultado = db.session.query(User).all()

                for linha in resultado:
                    print(linha)
                    if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Administrador":
                        return "administrador"
                    elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Usuário":
                        return "usuario"
                    else:
                        continue
                return "Sem acesso"
            except:
                return "administrador"

    #Método para realizar a remoção de um usuario do banco de dados
    def delete(self, user):
        with DBConnectionHandler() as db:
            try:
                db.session.query(User).filter(User.id == user).delete()
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return str(e)

    #Método para atualizar um usuario

    def update(self, user):

        with DBConnectionHandler() as db:
            db.session.commit()
            try:
                db.session.query(User).filter(User.name == user.name).update({User.name: user.name, User.password: user.password,
                         User.user: user.user, User.access: user.access})
                db.session.commit()
                return 'OK'
            except Exception as e:
                db.session.rollback()
                return str(e)