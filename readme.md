## FlaskApp | celery | SqlAlchemy

### Criar ambiente virtual | Ativar env | Instalar pacotes - Backend

```bash
python3 -m venv myenv &&
source myenv/bin/activate &&
pip install -r requirements.txt
```
### instalar fron-end

```bash
cd front-end/ && npm i
```

requisitos front-end:
npm 6.12.0
node 10.16.3
Deve estar instalado o vue-cli e vue-cli-service:
npm install -g @vue/cli
npm install -g @vue/cli-service-global

### Subir api
```bash
cd common/app && python views.py && echo'api no ar' 
```
### subir celery worker
```bash
cd common/app && celery -A views.celery worker --loglevel=info
```
### subir o front-end a app
```bash
cd front-end/ && npm run serve
```

#### Rodar o celery worker independete (arquivo tasks)
```bash
cd common/app
```
```bash
celery -A tasks worker --loglevel=info
```

```bash
python
```

```bash
from tasks import *
```

```bash
reverse.delay('mystring')
```

```bash
result = reverse.delay('mystring')
```

```bash
result.status
```

```bash
result.get()
```

```bash
result.ready()
```
