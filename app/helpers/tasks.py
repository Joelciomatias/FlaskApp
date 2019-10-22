''' from celery import Celery
import time
from celery.task.control import inspect
import threading


app = Celery('tasks',broker='amqp://localhost//',backend='db+mysql+pymysql://root:123456@localhost:3306/mydatabase')

@app.task
def reverse(string):
	time.sleep(2)
	return string[::-1]

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
 '''