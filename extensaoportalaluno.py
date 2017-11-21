from flask import Flask, render_template, request, url_for, redirect, flash
from config import SECURITY_REGISTERABLE, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from flask_sqlalchemy import SQLAlchemy
import flask_login
import Alunos
import time
import User

app = Flask(__name__)
app.secret_key = 'mude isso!'
db = SQLAlchemy(app)
app.secret_key = 'super secret string'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECURITY_REGISTERABLE'] = SECURITY_REGISTERABLE
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

login_manager = flask_login.LoginManager()

login_manager.init_app(app)



@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    email_Func = Alunos.Funcionario.query.filter_by(email=email).first()
    email_Alun = Alunos.Aluno.query.filter_by(email=email).first()
    if email_Func or email_Alun is None:
        return 

    user = User.User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form['email']
        email_Func = Alunos.Funcionario.query.filter_by(email=email).first()
        email_Alun = Alunos.Aluno.query.filter_by(email=email).first
        if request.form['password'] == email_Func.password or request.form['password'] == email_Alun.password:
            user = User.User()
            user.id = email
            flask_login.login_user(user)
            return redirect(url_for('protected'))


        return 'Bad login'

    return render_template('login.html')


@app.route('/protected')
@flask_login.login_required
def protected():
    flash('Logged in as: ' + flask_login.current_user.id)
    time.sleep(1)
    return redirect(url_for('index'))


@app.route('/')
@flask_login.login_required
def index():
    return render_template('index.html')

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))

@login_manager.user_loader
def user_loader(email):
    email_Func = Alunos.Funcionario.query.filter_by(email=email).first()
    email_Alun = Alunos.Aluno.query.filter_by(email=email).first
    if email_Func or email_Alun is None:
        return

    user = User.User()
    user.id = email
    return user

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('login'))

@app.route('/criar_tabelas')
def criar_tabelas():
    global db
    db.create_all()
    flash('criado com sucesso')
    return redirect(url_for('index'))

@app.route('/remover_tabelas')
def remover_tabelas():
    global db
    db.drop_all()
    flash('removido com sucesso')
    return redirect(url_for('index'))

@app.route('/post_user', methods=['POST'])
def post_user():
    user_func = Alunos.Funcionario(request.form['username'],
                              request.form['email'],
                              request.form['password'],
                              request.form['nome'],
                              request.form['endereco'],
                              request.form['cpf'],
                              request.form['mat_func'])

    user_alun = Alunos.Aluno(request.form['cpf'],
                              request.form['username'],
                              request.form['data_nasc'],
                              request.form['endereco'],
                              request.form['rg'],
                              request.form['email'],
                              request.form['password'])

    Alunos.db.session.add(user_func)
    Alunos.db.session.add(user_alun)
    Alunos.db.session.commit()
    flash('Usuario criado com sucesso')
    return redirect(url_for('index'))

@app.route('/admin_add')
def admin_add():
    return render_template('')

if __name__ == '__main__':
    app.run(debug=True)
