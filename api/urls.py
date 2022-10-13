from django.urls import path , include
from .views import *
from django.contrib.auth import views as auth_views
# from .api_old import *
from django.conf.urls import url


urlpatterns = [
    path('sc/', sc, name='sc'),
]