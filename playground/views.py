from django.shortcuts import render
from .tasks import notifiy_message


def say_hello(request):
    notifiy_message.delay('Hello Italy')
    return render(request, 'hello.html', {'name': 'Mosh'})
