from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from email_distribution.services import send_email

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@scheduler.scheduled_job('interval', days=1)
def schedule_email():
    send_email()
