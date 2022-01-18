from http.client import INSUFFICIENT_STORAGE
from flask import Flask, render_template, request, session, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlparse, urljoin

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))

login_manager = LoginManager()
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    db.init_app(app)

    login_manager.login_view = 'login'  # thanks to this, if user is not logged in and e.g. try to go to /profile - app will redirect him to login page
    login_manager.login_message = 'Hello dude, please log in to acces this page.'  # There I can change message for user if he try to go to some page, and he id not logged in.


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @app.route('/profile')
    @login_required
    def profile():
        return f'You are in the profile, {current_user.username}.'
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            user = User.query.filter_by(username=username).first()
            if not user:
                return 'User does not exist'
            login_user(user)

            if 'next' in session and session['next']:
                if is_safe_url(session['next']):
                    return redirect(session['next'])

            return redirect(url_for('index'))
        session['next'] = request.args.get('next')
        return render_template('login.html')
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return 'You now logged out!'
    
    @app.route('/')
    def index():
        return 'You on a home (index) page.'

    return app


# 1.
# How to create db? -> In activated venv in shell:
# from app import db, create_app, User
# db.create_all(app=create_app())
# fin :)
# exit()
# sqlite3 db.sqlite3
# .tables (and i should see my tables)
# .schema -> will show me schema of user model
#
# 2.
# And now after creating user 'Maciej' and
# go to the /login
# and then /profile - i should see my profile :)
#
# 3.
# 