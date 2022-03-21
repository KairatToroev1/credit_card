from django.utils import timezone
import threading
import time
from schedule import Scheduler

from .models import Cart_Credit


def status_card():
    for card in Cart_Credit.objects.all():
        if card.last_date_of <= timezone.now():
            card.card_status = Cart_Credit.StatusType.EXPIRED
            card.save()

def run_threaded(self,interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run


Scheduler.run_threaded = run_threaded

def start_scheduler():
    scheduler = Scheduler()
    scheduler.every(1).minutes.do(status_card())
    scheduler.run_pending()