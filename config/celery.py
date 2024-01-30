from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') # Установка переменной окружения для настроек проекта

app = Celery('config')  # Создание экземпляра объекта Celery

app.config_from_object('django.conf:settings', namespace='CELERY')  # Загрузка настроек из файла Django

app.autodiscover_tasks()  # Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
