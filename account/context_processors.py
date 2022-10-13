from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from .models import *
# from account.typing.models import Base_Company, Company

def base(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        up = UserProfile.objects.filter(user = current_user).first()
        context['base_user'] = current_user
        context['base_profile'] = up
        context['base_company'] =  Base_Company.objects.get(id = up.base_company_id)
        context['all_base_companies'] =  Base_Company.objects.all()
        # context['all_companies'] =  Company.objects.all()
    else:
        context['base_user'] = 'none'
        context['base_profile'] = 'none'
        context['base_company'] = 'none'
        context['all_base_companies'] = 'none'
        context['all_companies'] = 'none'
    return context

