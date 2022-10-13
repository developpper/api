from django.urls import path , include
from .views import *
from django.contrib.auth import views as auth_views
# from .api_old import *
from django.conf.urls import url


urlpatterns = [
    path('', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    # path('home', home, name='home'),
    # path('products', products, name='products'),
    path('users', users, name='users'),
    path('sc/', sc, name='sc'),

    # path('typing', typing, name='typing'),
    # path('typing/' , include('account.typing.urls')),
    # path('message/' , include('account.message.urls')),
    # path('freestyle/' , include('account.freestyle.urls')),

    path('api/' , include('account.urls_api')),
    # url('api/' , include('account.api.urls')),

     path('all-base-companies/', all_base_companies, name='all_base_companies'),
]