from flask import Flask, render_template, request
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy

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
            return 'You are logged in!'
        return render_template('login.html')
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return 'You now logged out!'

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