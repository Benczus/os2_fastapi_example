from time import sleep

from celery import Celery


tasks= Celery()


@tasks.task()
def sleep_task(duration):
    sleep(duration)
    return