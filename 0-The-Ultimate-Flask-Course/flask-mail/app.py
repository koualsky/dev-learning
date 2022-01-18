# ALL DOCUMENTATION: https://pythonhosted.org/Flask-Mail/

from flask import Flask
from flask_mail import Mail, Message

def create_app():
    app = Flask(__name__)

    # We need to create test account for this configurations - on some free service, like: fastmail.com
    # I just create there fake email and connect them with some fake device, e.g. - iphone
    app.config['MAIL_SERVER'] = 'smtp.fastmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'koualsky@fastmail.com'
    app.config['MAIL_PASSWORD'] = 'mnbtyywtmb2amdh3'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_DEFAULT_SENDER'] = ('KOUALSKY', 'koualsky@fastmail.com')  # 'koualsky@fastmail.com'  # i can just use only email as a string or tuple - if i want to add name to sender
    app.config['MAIL_MAX_EMAILS'] = 5  # (unnecessary) there i can specify how many email i'll send in one connection. after this connection will be closed and open again if we have more emails to send.

    mail = Mail()

    mail.init_app(app)

    @app.route('/')
    def index():
        msg = Message('Hello From Flask - this is subject! - see attachements!', 
            # sender=('Dupa', 'dupamurzyna@wp.com'),  # this field is isn't required. this is the second way that i can change the sender. but i need to have registered this user
            recipients=[
                'gaparo7159@whecode.com',
                # 'gaparo9917@whecode.com'
        ])  # and here i can use temporary email service to receive email, like: temp-mail.org
        # msg.add_recipient('gaparo1123@whecode.com')
        # msg.body = 'And this is the body of this message'  # this is standard txt message
        msg.html = '<p><strong>Hello</strong> Wrld :)</p><p>Please see attachement!</p><p>E<span style="color: red">nd</span>.</p>'  # but i can also send html messages (which is now standard) :)

        with app.open_resource('flask_cheatsheet.pdf') as pdf:
            msg.attach('my_flask_cheatsheet.pdf', 'application/pdf', pdf.read())  # i need to specify file type (from MIME types - search this in google)

        mail.send(msg)

        return 'Sent!'
    
    @app.route('/bulk')  # example how to sent bulk emails
    def bulk():
        users = [{'name': 'Maciej', 'email': 'maciej@email.com'}]  # This is users from db

        with mail.connect() as conn:
            for user in users:
                msg = Message('Bulk', recipients=[user['email']])
                msg.body = f'Hey {user["name"]}'
                conn.send(msg)

    return app

# if i want to have this mail functionality in debug mode i just need to make in my environment: export FLASK_ENV=development
# and after that i'll see logs in console