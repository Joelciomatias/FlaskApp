source myenv/bin/activate

cd common/app

python views.py

cd common/app &&

celery -A views.celery worker --loglevel=info

cd /front-end && npm run server