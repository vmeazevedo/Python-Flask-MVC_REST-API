from sql_alchemy import banco

class UserModel(banco.Model):
    # Nome da tabela
    __tablename__ = 'usuarios'

    # Cria as colunas da tabela
    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    # Construtor
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        
    # Função de retorno json
    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }
    
    @classmethod
    # Função para buscar no banco via query de select by id
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    # Função para salvar no banco	
    def save_user(self):
        banco.session.add(self)
        banco.session.commit()
    
    # Função para deletar do banco
    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
