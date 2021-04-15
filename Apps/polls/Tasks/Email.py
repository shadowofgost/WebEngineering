from __future__ import absolute_import, unicode_literals
from celery import shared_task
import datetime
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mass_mail
from django.core.mail import send_mail


@shared_task
def email():
    pass
