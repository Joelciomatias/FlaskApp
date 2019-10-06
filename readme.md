## FlaskApp | celery | SqlAlchemy

### Instalar pacotes
> pip install -r requirements.txt



#### Rodar o celery worker 
> celery -A tasks worker --loglevel=info
> python
> from tasks import *
> reverse.delay('mystring')
> result = reverse.delay('mystring')
> result.status
> result.get()
> result.ready()
