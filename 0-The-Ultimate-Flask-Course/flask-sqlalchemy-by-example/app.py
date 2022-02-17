# I can't get how to make relations... i can't get it. train it, slowly read, and make note about that.

from re import M
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

from datetime import datetime
from faker import Faker

import random

fake = Faker()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db.init(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    orders = db.relationship('Order', backref='customer')                             # second step to create relation - backreference


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)


order_product = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(50))

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)  # first step to create relation - relation to table (with id)
    products = db.relationship('Product', secondary=order_product)
    customer = db.relationship('Customer')  # a bie powinno tu teraz byc takiej relacji?


def add_customers():
    for _ in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.street_address(),
            city=fake.city(),
            postcode=fake.postcode(),
            email=fake.email()
        )
        db.session.add(customer)
    db.session.commit()


def add_orders():
    customers = Customer.query.all()
    for _ in range(50):
        customer = random.choice(customers)  # choose a random user

        ordered_date = fake.date_time_this_year()
        shipped_date = random.choices([None, fake.date_time_between(start_date=ordered_date)], [10, 90])[0]

        delivered_date = None
        if shipped_date:
            delivered_date = random.choices([None, fake.date_time_between(start_date=shipped_date)], [50, 50])[0]
        
        coupon_code = random.choices([None, '50OFF', 'FREESIPPING', 'BUYONEGETONE'], [80, 5, 5, 5])[0]

        order = Order(
            customer_id=customer.id,
            order_date=ordered_date,
            shipped_date=shipped_date,
            delivered_date=delivered_date,
            coupon_code=coupon_code
        )
        db.session.add(order)
    db.session.commit()


def add_products():
    for _ in range(10):
        product = Product(
            name=fake.color_name(),
            price=random.randint(10, 100)
        )
        db.session.add(product)
    db.session.commit()


def add_order_products():
    orders = Order.query.all()
    products = Product.query.all()
    for order in orders:
        k = random.randint(1, 3)
        purchased_products = random.sample(products, k)
        order.products.extend(purchased_products)
    db.session.commit()


# this function just aggregate all these above random data generators in one function. fullfill db with random data
# if i want fresh db - just empty db or remove sqlite3 file (if my db is sqlite)
def create_random_data():
    db.create_all()
    add_customers()
    add_orders()
    add_products()
    add_order_products()

# Populating the database
# 1. install: pip install faker
# 2. from faker import Faker  # in project, where we want to produce data for our development db.
# 3. fake = Faker()
# 4. after this we create function like above - add_customers() - and we can create that function for every model / table in our db :)
# 5. and how i can add some rows with relations, eg. for Orders? Just gen previously created customers and do the same as for add_customers() like in add_orders()


def get_orders_by(customer_id=1):
    print('Get Orders by Customer')
    customer_orders = Order.query.filter_by(customer_id=customer_id).all()
    for order in customer_orders:
        print(order.id)

def get_pending_orders():
    print('Pending Orders')
    pending_orders = Order.query.filter(Order.shipped_date.is_(None)).order_by(Order.order_date.desc()).all()
    for order in pending_orders:
        print(order.order_date)

def how_many_customers():
    print('How many customers')
    print(Customer.query.count())

def orders_with_code():
    print('Orders with coupon code')
    orders = Order.query.filter(Order.coupon_code.isnot(None)).all()
    for order in orders:
        print(order.coupon_code)

def revenue_in_last_x_days(x_days=30):
    print('Revenue past x days')
    print(db.session.query(db.func.sum(Product.price)).join(order_product).join(Order).filter(Order.order_date > (datetime.now() - timedelta(days=x_days))).all())
    # replace all() at the end with scalar() - for return only number

# 

def get_customers_who_have_purchased_x_dollars(amount=500):
    print('All customers who have')
    customers = db.session.query(Customer).join(Order).join(order_product).join(Product).group_by(Customer).having(db.func.sum(Product.price) > amount)
    for customer in customers:
        print(customer.first_name)
