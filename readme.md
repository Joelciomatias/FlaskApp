## FlaskApp | celery | SqlAlchemy

### Criar ambiente virtual
> python -m venv myenv
### Ativar env
> source myenv/bin/activate
### Instalar pacotes
> pip install -r requirements.txt
### Subir app
> python ./common/app/views.py

#### Rodar o celery worker (arquivo tasks)
> celery -A ./common/celery_tasks worker --loglevel=info

> python

> from tasks import *

> reverse.delay('mystring')

> result = reverse.delay('mystring')

> result.status

> result.get()

> result.ready()
