
import datetime
from flask import Flask
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import choice
from celery.task.control import inspect
from test_numpy import test_py
from flask_cors import CORS
from flask_socketio import SocketIO, join_room, emit
import threading
import random

# initialize Flask
app = Flask(__name__)
cors = CORS(app, resources={r"/*/": {"origins": "*"}})
socketio = SocketIO(app,cors_allowed_origins="*")

# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'db+mysql+pymysql://root:123456@localhost:3306/mydatabase'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/mydatabase'
celery = make_celery(app)

db = SQLAlchemy(app)

class TestPython(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    sum = db.Column('sum',db.Float())
    start = db.Column('start',db.DateTime())
    end = db.Column('end',db.DateTime())
    iterations = db.Column('iterations', db.Integer)

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
   # print(iterations,' iteration(s)')
    test_python.delay(iterations)
    return 'I sent a async task test python with %i interation(s)!' % iterations, 200

@celery.task(name='views.test_python')
def test_python(iterations):
    start = datetime.datetime.now()
    result = test_py(iterations)
    end = datetime.datetime.now()
    db.session.add(TestPython(sum=int(result),start=start,end=end,iterations=iterations))
    db.session.commit()
    print('Iniciado em: ',start,' \n Terminou em: ',end)
    return 'ok',200


@app.route('/queues-a')
def inspectQueues():
    i = inspect()
    active = {}
    active['active'] = i.active()
    return active,200

@app.route('/finished')
def get_finished_data():
    finished_data = TestPython.query.all()
    result = []
    for data in finished_data:
        result.append({
            'id':data.id,
            'sum':data.sum,
            'start':data.start,
            'end':data.end,
            'iterations':data.iterations,
        })
    _result = {}
    _result['result'] = result
    return _result,200

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def checkCelery():
    i = inspect()
    result = {}
    _active = i.active()
    reserved = i.reserved()
    if _active:
        for key in _active:
            if len(_active[key]) >= 0:
                result['active'] = _active[key]
                if reserved:
                    for _key in reserved:
                        if len(_active[key]) >= 0:
                            result['reserved'] = reserved[key]       
                    socketio.emit('active', result)
# set up the timer
set_interval(checkCelery, 1)

if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1', port='5000', debug=True)
