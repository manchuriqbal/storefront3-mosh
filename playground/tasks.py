from time import sleep
from celery import shared_task

@shared_task  
def notifiy_message(message):
    print('send 10k message')
    print(message)
    sleep(10)
    print('message ware succesfully send')