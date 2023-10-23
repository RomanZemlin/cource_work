import threading
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from email_distribution.services import send_email

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


def schedule_email():
    send_email()


scheduler.add_job(schedule_email, trigger=CronTrigger.from_crontab('0 9 * * *'))  # Здесь установлен запуск задачи каждый день в 9:00


def check_scheduler():
    while True:
        # Проверка состояния планировщика
        if scheduler.state == 'running':
            # Если активен, спать на 60 минут
            time.sleep(3600)
        else:
            # Если неактивен, включить планировщик
            scheduler.start()


# Запуск отдельного потока для проверки состояния планировщика
check_thread = threading.Thread(target=check_scheduler)

