from flask import Flask
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
#broker='amqp://localhost//',backend='db+mysql+pymysql://root:password@localhost:3306/search')ap
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'db+mysql+pymysql://root:password@localhost:3306/search'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/search_acync'
celery = make_celery(app)
db = SQLAlchemy(app)

class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data',db.String(50))
print(soma_args(3,4,4,4,4))
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I sent a string to async!'

@app.route('/insertData')
def insertData():
    insert.delay()
    return 'i sent a async request into database'

@celery.task(name='views.reverse')
def reverse(string):
    return string[::-1]

@celery.task(name='views.insert')
def insert():
    for i in range(5000):
        data = ''.join(choice('ABDCE') for i in range(50))
        result = Results(data=data)
        db.session.add(result)
    db.session.commit()
    return 'Foi!!!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)