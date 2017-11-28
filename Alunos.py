from extensaoportalaluno import db


class Funcionario(db.Model):

    id_func = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Funcionario %r %r %r>' % (self.username, self.email, self.password)


class Aluno(db.Model):

    id_alun = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, username, email, password, nome, telefone, endereco, cpf):

        self.username = username
        self.email    = email
        self.password = password
        self.nome     = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cpf      = cpf

    func_id  = db.Column(db.Integer, db.ForeignKey('funcionario.id_func'))
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id_alun'))

    funcionario = db.relationship('Funcionario', backref='user_func')

    def __repr__(self):
        return '<Funcionario %r %r %r %r %r %r %r >' % (self.username, self.email, self.password, self.nome, self.telefone, self.endereco, self.cpf)


class Curso(db.Model):

    id_curs = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(8), unique=True, nullable=False)
    nome_curso = db.Column(db.String(120), unique=True, nullable=False)
    qtnd_semestres = db.Column(db.Integer, nullable=False)

    def __init__(self, codigo, nome_curso, qtnd_semestres):
        self.codigo = codigo
        self.nome_curso = nome_curso
        self.qtnd_semestres = qtnd_semestres

    aluno_id= db.Column(db.Integer, db.ForeignKey('aluno.id_alun'))
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id_curs'))

    aluno = db.relationship('Aluno', backref='user_alun')

    def __repr__(self):
        return '<Curso %r %r %r>' % (self.codigo, self.nome_curso, self.qtnd_semestres)

class Disciplina(db.Model):

    id_disc = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(8), unique=True, nullable=False)
    nome_disc = db.Column(db.String(120), nullable=False)
    nota1_semes = db.Column(db.Float, nullable=False)
    nota2_semes = db.Column(db.Float, nullable=False)

    def __init__(self, codigo, nome_disc, nota1_semes, nota2_semes):
        self.codigo = codigo
        self.nome_disc = nome_disc
        self.nota1_semes = nota1_semes
        self.nota2_semes = nota2_semes

    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id_disc'))
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id_curs'))

    curso = db.relationship('Curso', backref='user_curs')

    def __repr__(self):
        return '<Disciplina %r %r %r %r>' % (self.codigo, self.nome_disc, self.nota1_semes, self.nota2_semes)

class Professores(db.Model):

    id_prof = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Funcionario %r %r %r>' % (self.username, self.email, self.password)

    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id_prof'))
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id_disc'))

    disciplian = db.relationship('Disciplina', backref='user_disc')

class Acesso(db.Model):

    id_acess = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Funcionario %r %r %r>' % (self.username, self.email, self.password)

    id_acesso = db.Column(db.Integer, db.ForeignKey('acesso.id_acess'))
    id_professor = db.Column(db.Integer, db.ForeignKey('professores.id_prof'))

    Profesores = db.relationship('Professores', backref='user_prof')