## FlaskApp | celery | SqlAlchemy

### Criar ambiente virtual
### Ativar env
### Instalar pacotes
"""python3 -m venv myenv &&
source myenv/bin/activate &&
pip install -r requirements.txt"""
### Subir api
"""cd common/app  && python views.py && echo'api no ar' """
### subir celery worker
"""cd common/app && celery -A views.celery worker --loglevel=info"""
### subir o front-end a app
"""cd front-end/ && npm i && npm run server"""

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
