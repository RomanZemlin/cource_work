from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from email_distribution.models import EmailDistribution
from email_distribution.services import send_email

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


email_distribution = EmailDistribution.objects.all()

if email_distribution:
    period = EmailDistribution.objects.latest('id')
else:
    period = 0


@scheduler.scheduled_job('interval', days=period)  # пример запуска функции каждую минуту
def schedule_email():
    send_email()