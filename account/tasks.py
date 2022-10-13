from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.contrib.auth.models import User

@shared_task
def add(x, y):
    return x + y


@shared_task
def data():
    user = User.objects.create_user(username = 'kkkk')
    user.save()
    # print(user_objs)