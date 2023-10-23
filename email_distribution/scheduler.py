from sched import scheduler

import pytz
import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from email_distribution.models import EmailDistribution
from email_distribution.services import send_and_log


def send_email():
    mailing_list = EmailDistribution.objects.all()
    now = datetime.datetime.now(pytz.timezone('UTC'))

    for obj in mailing_list:
        if obj.is_active and obj.status == 2 and obj.next <= now <= obj.finish:
            send_and_log(obj)
            if obj.period == '1':
                obj.next = now + datetime.timedelta(days=1)
            elif obj.period == '2':
                obj.next = now + datetime.timedelta(days=7)
            elif obj.period == '3':
                obj.next = now + datetime.timedelta(days=30)
            obj.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_email, 'interval', days=1)  # Интервал рассылки - каждый день
    scheduler.start()

if __name__ == '__main__':
    start()
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()