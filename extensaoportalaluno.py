from flask import Flask,render_template, request, url_for, redirect, flash
import User
import flask_login
import time


app = Flask(__name__)
app.secret_key = 'super secret string'

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'irineu@irineu.com': {'password': 'secret'}}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if request.form['password'] == users[email]['password']:
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
    if email not in users:
        return

    user = User.User()
    user.id = email
    return user

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
