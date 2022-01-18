# Remember, that migrations are always limited by my db system. For example - postgres.


# SQLAlchemy - models and orm (like django Model)
# Alembic - migration commands in migration files


#  BEGIN
# 1. After creating basic schema run command: `flask db init`
# 2. Then I can run migrations: `flask db migrate` -> after that I should see something in migrations/versions folder - thats creates for me migration file based on my model.
#    I should always check if everything is correct in this file. Because there is many db's and migration systems.
# 3. Then I can run `flask db upgrade` - and this command will upgrade my db according to my generated in previous step migration file.
# now i can check in my db if new table is appear :)


# UPGRADE - EVERY TIME I ADD SOME TO EXISTING MODEL OR I CREATE A NEW MODEL, RUN:
# 1. flask db migrate -> this command will generate only (raw sql?) commands that is changed in my models. only for update my db, not for creating new
#    then check this file, if this is right with raw sql commands, and then:
# 2. flask db upgrade -> then check changes in db


# DOWNGRADE - if i want to step back, make only one downgrade at time. and make that step by step.
# In every migration file I should have downgrade section which section should reverse all changes that we added in this particular migration file
# After I run `flask db downgrade` - I should have my db version before last migration file :) and if I want to have this change permanently - i should also remove migration file, and changes in models.

# And if after downgrade I'll again run upgrade - I again should have my db in primary version :D

# But usually if i want to remove something in worked system. I need to make changes on model, then generate migration file that remove this (and restore in downgrade xD) and then make upgrade.


# for testing postgres i can use elephantsql.com


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()  # SQLAlchemy is the same thing as Model in django. This is just ORM. But more flexible ORM.
migrate = Migrate()


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))  # added later, for another migration file purpose


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)


def create_app():
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dvnimpjf:hu0e5enc9j9oQf5LowJLtZX6fwNvguis@tyke.db.elephantsql.com/dvnimpjf'  # this is the only change to change db to postgres :p (and install psycopg2-binary)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  # and this is only for using postgres :) without this will not work.

    db.init_app(app)
    migrate.init_app(app, db)

    return app



# generally - i should create migration files, like `flask db migrate` if i change something in my models
# i should run `flask db upgrade` everytime if i want to introduce my changes from models to my database. if i switch db, i don't need to make migrations. only upgrade.








# ! Manually edit migration file - example
# In some situations we need to manually change migration file. e.g.:
# If we want for example change model name from Order to Orders, sqlalchemy will automaticly drop all 'Order' table, and create new 'Orders' table.
# So in that way we lost all data! o_O 
# So! We need to edit migration file. If I need something to do -> check alembic documentation
# If I want to rename some table, I need to use rename_table. So all I need to do in that situation (rename table name), is:
# (remember that every alembic command starts with op - operation - imported command from alembic lib)
# first: remove all standard changes that sqlalchemy are put in my migration file, and:
# in upgrade section of migration file: op.rename_table('order', 'orders')
# in downgrade section of migration file: op.rename_table('orders', 'order') - opposite operations that we make in upgrade section.
# and after that: `flask db upgrade`