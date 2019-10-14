## FlaskApp | celery | SqlAlchemy

### Criar ambiente virtual | Ativar env | Instalar pacotes - Backend
```python3 -m venv myenv &&
source myenv/bin/activate &&
pip install -r requirements.txt```
### instalar fron-end
```cd front-end/ && npm i```

requisitos front-end:
npm 6.12.0
node 10.16.3
Deve estar instalado o vue-cli e vue-cli-service:
npm install -g @vue/cli
npm install -g @vue/cli-service-global

### Subir api
```cd common/app && python views.py && echo'api no ar' ```
### subir celery worker
```cd common/app && celery -A views.celery worker --loglevel=info```
### subir o front-end a app
```cd front-end/ && npm run serve```

#### Rodar o celery worker independete (arquivo tasks)
```cd common/app```
```celery -A tasks worker --loglevel=info```

```python```

```from tasks import *```

```reverse.delay('mystring')```

```result = reverse.delay('mystring')```

```result.status```

```result.get()```

```result.ready()```
