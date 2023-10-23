from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from email_distribution.services import send_email

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@scheduler.scheduled_job('interval', minutes=1)  # пример запуска функции каждую минуту
def schedule_email():
    send_email()