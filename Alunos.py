from extensaoportalaluno import db

class Funcionario(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable= False)
    nome     = db.Column(db.String(120), nullable=False)
    endereco = db.Column(db.String(120), nullable=False)
    cpf      = db.Column(db.Integer, unique=True, nullable=False )
    mat_func = db.Column(db.Integer, unique= True, nullable=False)

    def __init__(self, username, email, password, nome, endereco, cpf, mat_func):
        self.username = username
        self.email    = email
        self.password = password
        self.nome     = nome
        self.endereco = endereco
        self.cpf      = cpf
        self.mat_func = mat_func

    def __repr__(self):
        return '<User %r %r %r %r %r %r %r>' % (self.username, self.email, self.password, self.nome, self. endereco, self.cpf, self.mat_func)
