## FlaskApp | celery | SqlAlchemy | vueApp

### Criar ambiente virtual | Ativar env | Instalar pacotes - Backend

```bash
python3 -m venv myenv &&
source myenv/bin/activate &&
pip install -r requirements.txt
```
### database 

> criar a database mydatabase no mysql

Rodar o alembic:


```bash
alembic upgrade head
```


### instalar fron-end - 

```bash
cd front-end/ && npm install
```

requisitos front-end:

> npm 6.12.0

> node 10.16.3

> Deve estar instalado o vue-cli e vue-cli-service:

```bash
npm install -g @vue/cli
```

```bash
npm install -g @vue/cli-service-global
```

### Subir api
```bash
python run.py 
```

### subir celery worker
```bash
cd app && celery -A views.celery worker --loglevel=info
```

### subir o front-end
```bash
cd front-end/ && npm run serve
```

