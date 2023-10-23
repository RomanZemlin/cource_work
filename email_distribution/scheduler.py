import threading
import time
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from email_distribution.models import EmailDistribution
from email_distribution.services import send_email

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


def schedule_email():
    send_email()


def check_scheduler():
    while True:
        # Проверка состояния планировщика
        if scheduler.state == 'running':
            # Если активен, спать на 60 минут
            time.sleep(3600)
        else:
            # Если неактивен, включить планировщик
            scheduler.start()
            # Здесь можно добавить дополнительную логику, например, получение новых значений из формы или проверка условий для активации планировщика


# Запуск отдельного потока для проверки состояния планировщика
check_thread = threading.Thread(target=check_scheduler)
