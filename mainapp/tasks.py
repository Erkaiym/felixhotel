# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_user_email(title, message, email):
    send_mail(
        title,
        message,
        email,
        ['Hotel2kg@gmail.com'],
        fail_silently=False,
    )
    return True
