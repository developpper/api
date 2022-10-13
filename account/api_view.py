from django.shortcuts import render
from django.http import JsonResponse    
from django.contrib.auth.models import User
from .models import *

import json

# index
def index(request):
    return render(request, 'index.html')


# ajax_posting function
def ajax_posting(request):
    if request.is_ajax():
        first_name = request.POST.get('first_name', None) # getting data from first_name input 
        last_name = request.POST.get('last_name', None)  # getting data from last_name input
        if first_name and last_name: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON


def add_user(request):
        if request.is_ajax():
            us = User.objects.filter(username=request.POST.get("username")).first()
            # print(us)
            if us:
                response = {
                'error':'Username already exist. Please select new one.' # response message
                    }
                return JsonResponse(response)  
            else:
                user = User.objects.create_user(first_name=request.POST.get("first_name"),last_name=request.POST.get("last_name"),username=request.POST.get("username"),email=request.POST.get("email"),password=request.POST.get("password"))
                # print(request.POST.get("file"))
                user.save()
                bs_com = Base_Company.objects.get(id=request.POST.get("base_company"))
                userp = UserProfile.objects.create(role=request.POST.get("role"),mobile=request.POST.get("mobile"),user = user, base_company=bs_com )
                userp.save()
                print(user)
                response = {
                    'msg':'User has been registered.' # response message
                }
                return JsonResponse(response) 



def user_detail(request):
        if request.is_ajax():
            user_id = request.POST.get("id")
            user = User.objects.filter(id = user_id).first()
            us_p = UserProfile.objects.get(user_id = user.id)
            # print(us_p.base_company)
            base_co = Base_Company.objects.get(company_name = us_p.base_company)
            # print(base_co.id)
            response = {'id' : user.id, 'first_name' : user.first_name , 'last_name' : user.last_name , 'username' : user.username , 'email' : user.email , 'role' : us_p.role , 'mobile' : us_p.mobile , 'base_company_id' : base_co.id, 'base_company_name' : base_co.company_name}
            # print(type(response))
            return JsonResponse(response) 


def edit_user(request):
        if request.is_ajax():
            user = User.objects.create_user(first_name=request.POST.get("first_name"),last_name=request.POST.get("last_name"),username=request.POST.get("username"),email=request.POST.get("email"),password=request.POST.get("password"))
            user.save()
            userp = UserProfile.objects.create(role=request.POST.get("role"),mobile=request.POST.get("mobile"),user= user)
            userp.save()
            print(user)
            response = {
                'msg':'User has been registered.' # response message
            }
            return JsonResponse(response) 


def update_user(request):
        if request.is_ajax():
            user_id = request.POST.get("id")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            role = request.POST.get("role")
            mobile = request.POST.get("mobile")
            base_company = request.POST.get("base_company")
            user = User.objects.get(id = user_id)
            us_p = UserProfile.objects.get(user_id = user.id)
            cp_b = Base_Company.objects.get(id = base_company)
            user.username = username
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if password:
                user.set_password(password)
            if email:
                user.email = email
            if mobile:
                us_p.mobile = mobile
                us_p.save()

            us_p.role = role
            us_p.base_company = cp_b
            us_p.save()
            user.save()
            print(user)
            response = {'id' : user.username, 'msg':'User has been registered.' # response message
            }
            return JsonResponse(response) 


def delete_user(request):
        if request.is_ajax():
            id1 = request.GET.get('id', None)
            User.objects.get(id=id1).delete()
            data = {
            'deleted': True
            }
            return JsonResponse(data)



def get_all_company_base(request):
    if request.is_ajax():
       all_companies = Base_Company.objects.values('id','company_name')
       response = {
           'data': list(all_companies), 
        }
    else:
        print('nooooooooooooo')
        response = {
           'msg':'error' 
        }
    return JsonResponse(response) 




def add_base_company(request):
    if request.is_ajax():
        company_name = request.POST.get('company_name') # getting data from first_name input 
        address_1 = request.POST.get('address_1')  # getting data from last_name input
        address_2 = request.POST.get('address_2')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        website = request.POST.get('website')
        base_url = request.POST.get('base_url')
        if request.FILES:
            logo = request.FILES['logo_file']
            q_items = Base_Company.objects.create(company_name = company_name, address_line_1 =address_1 , address_line_2 = address_2 , email = email, mobile = mobile , website = website , base_url = base_url , logo = logo )
        else:
            q_items = Base_Company.objects.create(company_name = company_name, address_line_1 =address_1 , address_line_2 = address_2 , email = email, mobile = mobile , website = website , base_url = base_url )
        q_items.save()
        print(q_items)
        response = {
           'msg':'Your form has been submitted successfully' # response message
        }
        return JsonResponse(response) # return response as JSON
    else:
        print('kkkwork')
        response = {
           'msg':'error' # response message
        }
        return JsonResponse(response) # return response as JSON


def update_base_company(request):
    if request.is_ajax():
        i_id = request.POST.get('i_id')
        company_name = request.POST.get('company_name')
        address_1 = request.POST.get('address_1') # getting data from first_name input 
        address_2 = request.POST.get('address_2')  # getting data from last_name input
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        website = request.POST.get('website')
        base_url = request.POST.get('base_url')
        if len(request.FILES) != 0:
            logo = request.FILES['file']
            # q_items = Base_Company.objects.filter(id = i_id).update(company_name = company_name, address_line_1 =address_1 , address_line_2 =address_2, email = email, mobile = mobile , website = website, logo = logo  )
            q = Base_Company.objects.get(id = i_id)
            q.company_name = company_name
            q.address_line_1 =address_1 
            q.address_line_2 =address_2
            q.email = email
            q.mobile = mobile
            q.website = website
            q.logo = logo
            q.base_url = base_url
            q.save()
        else:
            q_items = Base_Company.objects.filter(id = i_id).update(company_name = company_name, address_line_1 =address_1 , address_line_2 =address_2, email = email, mobile = mobile , website = website, base_url = base_url)
            print(q_items)
        response = {
           'msg':'Your form has been submitted successfully' # response message
        }
        return JsonResponse(response) # return response as JSON
    else:
        print('kkkwork')
        response = {
           'msg':'error' # response message
        }
        return JsonResponse(response) # return response as JSON



def delete_base_company(request):
    if request.is_ajax():
            id1 = request.GET.get('id', None)
            Base_Company.objects.filter(id=id1).delete()
            data = {
            'deleted': True
            }
            return JsonResponse(data)





def edit_base_company(request):
    if request.is_ajax():
        id = request.POST.get('id', None)
        print(id)
        data = Base_Company.objects.filter(id=id).first()
        
        return JsonResponse({'id' : data.id , 'company_name' : data.company_name , 'address_line_1' : data.address_line_1 , 'address_line_2' : data.address_line_2 , 'website' : data.website , 'email' : data.email , 'mobile' : data.mobile })

