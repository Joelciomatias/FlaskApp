## FlaskApp | celery | SqlAlchemy

### Criar ambiente virtual
> python3 -m venv myenv
### Ativar env
> source myenv/bin/activate
### Instalar pacotes
> pip install -r requirements.txt
### Subir app
> cd common/app
> python views.py
### subir celery worker
> cd common/app
> > cd common/app
> python views.py

#### Rodar o celery worker independete (arquivo tasks)
> cd common/app
> celery -A tasks worker --loglevel=info

> python

> from tasks import *

> reverse.delay('mystring')

> result = reverse.delay('mystring')

> result.status

> result.get()

> result.ready()
