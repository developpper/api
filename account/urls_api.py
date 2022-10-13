from django.conf.urls import url
# from rest_framework_simplejwt import views as jwt_views
from django.urls import path

from .api_view import *

urlpatterns = [
    # path('', index),
    path('ajax-posting/', ajax_posting, name='ajax_posting'),
    path('add-user/', add_user, name='add_user'),
    path('delete-user',  delete_user, name='delete_user'),
    path('user_detail',  user_detail, name='user_detail'),
    path('edit-user',  edit_user, name='edit_user'),
    path('update-user',  update_user, name='update_user'),

    path('get-all-company_base/', get_all_company_base, name='get_all_company_base'),

    path('add-base-company/', add_base_company, name='add_base_company'),
    path('edit-base-company/', edit_base_company, name='edit_base_company'),
    path('update-base-company/', update_base_company, name='update_base_company'),
    path('delete-base-company/', delete_base_company, name='delete_base_company'),
]