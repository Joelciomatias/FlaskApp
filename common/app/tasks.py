from celery import Celery
import time

app = Celery('tasks',broker='amqp://localhost//',backend='db+mysql+pymysql://root:123456@localhost:3306/mydb')

@app.task
def reverse(string):
	time.sleep(2)
	return string[::-1]

