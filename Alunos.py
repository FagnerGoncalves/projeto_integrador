from flask_sqlalchemy import SQLAlchemy
from extensaoportalaluno import app

db = SQLAlchemy(app)

class Alunos(db.Model):
    id = db.Column('aluno_id', db.Integer)
    nome = db.Column(db.String(100))

    def __repr__(self):
        return '<User %r>' % (self.nome)