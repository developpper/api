from django.shortcuts import render

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import logout , authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *


# def home(request):
#     if request.user.is_authenticated():
#         print('auth')
#         # return render(request , 'home.html')
#     else:
#        print('not auth')
#     #    return render(request , 'home.html')


# def home(request):
#     if request.user.is_authenticated:
#         print('yes the user is logged-in')
#         return render(request , 'home.html')
#     else:
#         print('no the user is not logged-in')
#         return redirect("{{ url : 'account' }}")


def login_request(request):
  if request.user.is_authenticated:
    usr = UserProfile.objects.filter(user = request.user).first()
    # bs = UserProfile.objects.get(id = usr)
    # print(bs)
    bs = UserProfile.objects.get(id = usr.id)
    print(type(bs.base_company))

    base = Base_Company.objects.get(id = bs.base_company.id)
    print(base.base_username)
    # messages.info(request, f"You are now logged in as {username}")
    return redirect(base.base_username)
    # if usr.role == 'admin':
    #     return redirect("typing")  
    # else:
    #    return redirect("typing") 
  else:
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # print('don')
                login(request, user)
                bs = UserProfile.objects.get(id = user.id)
                print(type(bs.base_company))

                base = Base_Company.objects.get(id = bs.base_company.id)
                # print(base.base_username)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect("users")
                # return redirect("typing") 

            else:
                print('no yar')
                messages.info(request, "No User Found!")
        # else:
            #  messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    form.fields['username'].widget.attrs['class'] = "input"
    
    form.fields['password'].widget.attrs['class'] = "input"
    # form.help_text = None
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})


def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect("login")


# def products(request):
#     if request.user.is_authenticated:
#         return render(request , 'products.html')
#     else:
#         print('no the user is not logged-in')
#         return redirect("/account")


def typing(request):
    if request.user.is_authenticated:
        return render(request , 'typing/home.html')
    else:
        print('no the user is not logged-in')
        return redirect("/account")


@login_required(login_url='login')
def users(request):
    usr = UserProfile.objects.filter(user = request.user).first()
    if usr.role == 'admin':
        context = {}
        try:
            user_objs = User.objects.all()
            context['user_objs'] =  user_objs
            user_role = UserProfile.objects.all(user = user_objs)
            context['user_role'] =  user_role
        except Exception as e: 
            print(e)

        # print(context)
        return render(request , 'users.html' ,context)
    else:
        return redirect("login")




@login_required(login_url='login')
def all_base_companies(request):
    usr = UserProfile.objects.filter(user = request.user).first()
    if usr.role == 'admin':
        context = {}
        try:
            q_objs = Base_Company.objects.all()
            context['companies'] =  q_objs
        except Exception as e: 
            print(e)
        # print(context)
        return render(request , 'base_companies.html' ,context) 

    return redirect('users')



def sc(request):
    print('hello')
    return render(request, 'index.html')