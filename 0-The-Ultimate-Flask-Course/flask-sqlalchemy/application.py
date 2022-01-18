# To run this app i need to run some postgres instance (somewhere in internet i can find free instances)
# like: https://customer.elephantsql.com, and put his config in my config.cfg file.
# And open this db in some db viewer like dbeaver
# at the end - add this example file to my dev-learning repo!

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)  

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(50))
    join_date = db.Column(db.DateTime)

    orders = db.relationship('Order', backref='member', lazy='dynamic')
    courses = db.relationship('Course', secondary='user_courses', backref='member', lazy='dynamic')

    def __repr__(self):
        return f'<Member {self.username}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    # here we create relationship between Member and Order :) We just connect this Order to some Member.
    # i think that called this field should be like table for what we create relation. so - member :)
    # everytime we create relationship we need to create back relation in Member (orders = db.relationship...)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

db.Table('user_courses', 
    db.Column('member_id', db.Integer, db.ForeignKey('member.id')), 
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
    )

if __name__ == '__main__':
    app.run()


# PRE
# we can easily connect to the postgres database through psycopg2 and use clear sql to communicate with them 
# or we can easily configure sql alchemy with postgres like above!



# Creating tables from this above models ?
# just run python console in project env and import db.
# then just db.create_all() - thats it! fin.


# Add something to table
# maciej = Member(username='maciej', password='maciej', email='maciej@email.com', join_date=datetime.today())
# db.session.add(maciej)  # we can add like this several things
# db.commit()  # will save to the db all objects in session :)

# Update soma data? - Just get some object and update it
# alice = Member.query.filter(Member.username == 'alice').first()
# alice.password = 'dupa'
# maciej.password = 'wielka'
# db.session.sommit  # in this way i can change several objects in session and then update db by one request with this command :)

# Deleting
# db.session.delete(maciek)  # we should first get this object from db by querying like below
# db.session.commit()

# Querying

# (few words about queries)
# Member.query.filter(...) - gives us only query object. If we want to execute this object, we should use .first(), .all() at the end.
# first() will return that object from db, and all() will return list of objects.

# filter_by - for simple purposes
# jan = Member.query.filter_by(username='jan').first()  # it is good for simple queries, filters
# similars = Member.query.filter(or_(Member.username == 'maciej', Member.username == 'mariusz'))
# # usually we should to use this method. it is more powerfull (and we receive query we can iterate over it or use .all() 
# at the end an we have list of objects)

# filter - for advanced queries

# like
# Member.query.filter(Member.username.like('%ac%') - will return us every member with 'ac' in his username.

# in_
# Member.query.filter(Member.username.in_(['maciej', 'Mike'])) - will return everything that pass that what i have in list

# not in
# Member.query.filter(~Member.username.in_(['maciej', 'Mike'])) - wille return everything besides this two usernames (only add tilda!) tilda represents not

 # == and !=
 # Member.query.filter(Member.email == None) - will show us every user with empty email field
 # Member.query.filter(Member.email != None) - will show us every user with filled email field

# multiple filters (three different ways to use)
# Member.query.filter(Member.username == 'maciej').filter(Member.email == 'maciej@email.com') - will return members with username 'maciej' and that given email
# Member.query.filter(Member.username == 'maciej', Member.email == 'maciej@email.com') - the same effect.
# Member.query.filter(db.and_(Member.username == 'maciej', Member.email == 'maciej@email.com')) - the same effect.

# or_
# Member.query.filter(db.or_(Member.username == 'maciej', Member.username == 'Mike')) - return all members with username 'maciej' or 'Mike'
# Member.query.filter(db.or_(Member.username == 'maciej', Member.email == None)) - second example with username 'maciej' or with empty email field



# order_by - for ordering results in query
# Member.query.order_by(Member.username)
# Member.query.order_by(Member.id)
# and so on.

# limit
# Member.query.limit(3)
# Member.query.filter(Member.username == 'julia').limit(10)

# offset - just skip first 'x' results
# Member.query.offset(5)

# count
# Member.query.count() - will count and return to us how many results we have

# inequality
# Member.query.filter(Member.id >= 3)
# Member.query.filter(Member.email < 'c') - will return every email start with 'a', 'b' and 'c'.
# Member.query.filter(Member.email > 'c') - will return every email start with 'c', 'd', 'e' and so on.

# RELATIONSHIPS
# relational databases are very excellent in creating relationships between tables. There are 3 main relationships:

# One To Many
# create relationship like above in Order
# create backref in Member 
# now we can create Order like: order1 = Order(price=50, member_id=maciej.id)
# or: order2 = Order(price=50, member=maciej)  # we give all object!
# and now!: maciej.orders.all() - will show us all Member Orders :)

# Many To Many
# ...models like above and queries can be like this:
# course1 = Course(name='Course One')  # and create like that 3 courses
# then get 2 members, eg. maciej and michelle
# course1.member.append(maciej)
# course1.member.append(michelle)
# course1.member  # and this give us: [<Member maciej>, <Member michelle>]
# db.session.commit() - and see now how it looks in out db :)
# also: maciej.courses.all() - :)

# we can konow what courses i have by:
# maciej.courses.all() - [<Course 1>]

# or we can know what users have particular course by:
# course1.member  - [<Member maciej>, <Member michelle>]







# Want to experiment with theese app? Just run venv, python and then from application import db, Member, Order, Course and have fun!