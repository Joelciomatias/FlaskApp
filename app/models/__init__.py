from app import factory
import app


app = factory.create_app(celery=app.celery)