from celery import Celery

def make_celery(app_name=__name__):
    backend = "db+mysql+pymysql://root:123456@localhost:3306/mydatabase"
    broker = "amqp://localhost//"
   
    return Celery(app_name, backend=backend, broker=broker)

celery = make_celery() 