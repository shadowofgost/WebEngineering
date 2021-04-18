from __future__ import absolute_import, unicode_literals
from celery import shared_task
import datetime
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mass_mail
from django.core.mail import send_mail


@shared_task
def add(x, y):
    res = x + y
    time_format = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('当前时间为：' + time_format + ' ,两个数相加的结果为：')
    message = 'Here is the message'+time_format
    send_mail('Test', message, 'shadowofgost@outlook.com',
              ['2382510536@qq.com'], fail_silently=False)
    return res
