from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField, Form, FormField, FieldList, ValidationError, DateField
from wtforms import validators
from wtforms.validators import InputRequired, Length, AnyOf, Email


class TelephoneForm(Form):  # I need to inheritate from Form If I want to use this form IN FlaskForm
    country_code = IntegerField('country_code')
    area_code = IntegerField('area_code')
    number = StringField('number')


class YearForm(Form):
    year = IntegerField('year')
    total = IntegerField('total')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[  # the first 'username' is just label (in frontend - html)
        InputRequired(), 
        Length(min=3, max=8),
    ])
    password = PasswordField('password', validators=[
        InputRequired(), 
        AnyOf(values=['secret', 'password'])
    ])
    dupa = SelectField('dupa', choices=[('cpp', 'C++'), ('py', 'Python'), ('js', 'JavaScript')])
    age = IntegerField(label='Your age', default=18)  # strict way
    email = StringField('email', validators=[Email()])


class NameForm(LoginForm):  # This class is only to show, that I can inheritate from another form class
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    home_phone = FormField(TelephoneForm)  # todo: look at this! u see that? we have form in form! -> look at the frontend template how to use this.
    years = FieldList(FormField(YearForm), min_entries=3)

    # in that way i can make my own custom validation
    def validate_first_name(form, field):
        if field.data != 'Maciej':
            raise ValidationError('You do not have the right name.')


class DynamicForm(FlaskForm):
    entrydate = DateField('entrydate')#, format='%d/%m/%Y')  # format argument is optional (but if i change this format - placeholder wont!)


class User:
    def __init__(self, username, age, email):
        self.username = username
        self.age = age
        self.email = email


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Mysecret!'
    app.config['WTF_CSRF_ENABLED'] = True  # The True is by default. Usually we always use csrf token.
    app.config['WTF_CSRF_TIME_LIMIT'] = 3600  # 3600 sec. is default value (1h) If i'll set here e.g. 10, - csrf token for this form will be available only for 10 seconds.
    # After this time I'll receive csrf expired error. (I need to also handle csrf_token errors on frontend - template)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        # ! this is another way to use all object to the form :)
        user = User(username='John', age=50, email='john@doe.com')
        # form = LoginForm(obj=user)  # like that i can prepopulate form
        form = NameForm(obj=user)  # like that i can prepopulate form
        # form = LoginForm(email='one@two.com')  # i can use here my inputs for form directly! Like LoginForm(email='one@two.com') - that can be also default value!



        if form.validate_on_submit():
            output = f'''<h1>
            Username: {form.username.data}, 
            First name: {form.first_name.data}, 
            Last name: {form.last_name.data}, 
            Password: {form.password.data}, 
            Dupa: {form.dupa.data}, 
            Age: {form.age.data}, 
            Email: {form.email.data},
            Country Code: {form.home_phone.country_code.data},  # zwykle zagniezdzanie...
            Area Code: {form.home_phone.area_code.data},
            Number: {form.home_phone.number.data}
            '''

            for field in form.years:
                output += f'Year: {field.year.data} '
                output += f'Total: {field.total.data} <br />'
            
            output += '</h1>'
            return output

        return render_template('index.html', form=form)

    # This route was created for showing how dynamic forms are easy in use
    @app.route('/dynamic', methods=['GET', 'POST'])
    def dynamic():
        DynamicForm.name = StringField('name')

        names = ['middle_name', 'last_name', 'nickname']

        for name in names:
            setattr(DynamicForm, name, StringField(name))

        form = DynamicForm()

        if form.validate_on_submit():
            return f'Name: {form.name.data}, Last Name: {form.last_name.data}, Date: {form.entrydate.data}'

        return render_template('dynamic.html', form=form, names=names)

    return app
