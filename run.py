import os 
os.system('python app/views.py')
os.system('cd app && celery -A views.celery worker --loglevel=info')
