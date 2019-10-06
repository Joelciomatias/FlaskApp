from celery import Celery
import time
#app = Celery('tasks',broker='redis://localhost')
app = Celery('tasks',broker='amqp://localhost//',backend='db+mysql+pymysql://root:password@localhost:3306/search')

@app.task
def reverse(string):
	time.sleep(10)
	return string[::-1]

