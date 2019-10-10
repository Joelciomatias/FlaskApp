import datetime
from flask import Flask
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import choice
from test_numpy import test_py

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'db+mysql+pymysql://root:123456@localhost:3306/mydb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/mydb'
celery = make_celery(app)

db = SQLAlchemy(app)

class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data',db.String(50))

class TestPython(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    sum = db.Column('sum',db.Float())
    start = db.Column('start',db.DateTime())
    end = db.Column('end',db.DateTime())
    interations = db.Column('interations', db.Integer)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/process/<name>')
def process(name):
    print(name)
    reverse.delay(name)
    return 'I sent a string to async!'

@celery.task(name='views.reverse')
def reverse(string):
    return string[::-1]

@app.route('/test-python/')
@app.route('/test-python/<int:iterations>')
def test_python_task(iterations=1):
    print(iterations,' iteration(s)')
    test_python.delay(iterations)
    return 'I sent a async task test python with %i interation(s)!' % iterations, 200

@celery.task(name='views.test_python')
def test_python(interations):
    start = datetime.datetime.now()
    result = test_py(interations)
    # print(int(result),type(result))
    end = datetime.datetime.now()
    db.session.add(TestPython(sum=int(result),start=start,end=end,interations=interations))
    db.session.commit()
    print('Iniciado em: ',start,' \n Terminou em: ',end)
    return 'ok',200

@app.route('/insertData')
def insertData():
    insert.delay()
    return 'i sent a async request into database'

@celery.task(name='views.insert')
def insert():
    for i in range(500):
        data = ''.join(choice('ABDdsfgsdfgdCE') for i in range(50))
        result = Results(data=data)
        db.session.add(result)
    db.session.commit()
    return 'Foi!!!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)