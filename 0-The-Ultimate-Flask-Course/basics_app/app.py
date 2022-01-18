from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'

def connect_db():
    sql = sqlite3.connect('data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/hello/<name>')
def index(name):
    return f'<h1>Hello {name}!</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'DEFAULT'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name

    db = get_db()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()

    return render_template('home.html', name=name, display=False, \
            mylist=[1, 2, 'dupa', 3], listofdicts=[{'name': 'Zac'}, {'name': 'Zoe'}], results=results)
    # return f'<h1>Yolo {name} dude!</h1>'

@app.route('/popsession')
def popsession():
    session.pop('name', None)
    return 'session was cleaned'

@app.route('/json')
def json():
    dupa = [1, 2, 'x', 'y', 'z']
    name = session['name']
    return jsonify({'key': 'value', 'listkey': [1, 2, 3], 'name': name})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h1>Hi {name} you are on the {location}!</h1>'

@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
        # return '''<form method="POST" action="/theform">
        #             <input type="text" name="name">
        #             <input type="text" name="location">
        #             <input type="submit" value="Submix">
        #         </form>'''
    else:  # POST
        name = request.form['name']
        location = request.form['location']
        db = get_db()
        db.execute('insert into users (name, location) values (?, ?)', [name, location])
        db.commit()
        #return f'Hello <b>{name}</b>. You are from <b>{location}</b>. U R submitted the form successfully dude!'
        print('saved to the db and redirect...')
        return redirect(url_for('home', name=name, location=location))
'''
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return f'Hello <b>{name}</b>. You are from <b>{location}</b>. You are submitted the form successfully.'
'''

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    return jsonify({'result': 'Success!', 'name': name, 'location': location, 'randomlist': randomlist})

@app.route('/viewresults')
def viewresults():
    db = get_db()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()
    html = ''
    for r in results:
        html += '<p>The ID is <b>{}</b>. The name is <b>{}</b>. The location is <b>{}</b>.</p>'.format(r['id'], r['name'], r['location'])
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

