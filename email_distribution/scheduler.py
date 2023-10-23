from sched import scheduler

from apscheduler.schedulers.background import BackgroundScheduler

from email_distribution.services import send_email


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_email, 'interval', days=1)  # Интервал рассылки
    scheduler.start()

if __name__ == '__main__':
    start()
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()