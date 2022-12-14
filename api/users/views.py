from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import *
from django.contrib.auth.models import User
from account.models import UserProfile, Base_Company


@api_view(['POST'])
def login_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    print(email)

    try:
        if email is None:
            return Response({
                'detail': 'Email field is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        if password is None:
            return Response({
                'detail': 'Password field is required'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        user = authenticate(username=email, password=password)

        # user = authenticate(email=email, password=password)

        u = User.objects.get(username=user)
        user_id = u.id
        se = UserProfile.objects.get(user_id=user_id)
        # print(se)
        base = Base_Company.objects.get(id=se.base_company_id)

        print(base.company_name)

        if not user:
            return Response({
                'detail': 'Invalid Credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        serializer = UserInfoSerializer(user)

        return Response({
            'user': serializer.data,
            'token': token.key,
            'base_company': base.company_name,
            'base_company_url': base.base_url
        })
    except:
        return Response({
            'detail': 'Oops, something went wrong-1!'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# @api_view(['POST'])
# def login_user(request):
#     email = request.POST.get('email')
#     password = request.POST.get('password')

#     print(email)

#     try:
#         if email is None:
#             return Response({
#                 'detail': 'Email field is required'
#             }, status=status.HTTP_400_BAD_REQUEST)
#         if password is None:
#             return Response({
#                 'detail': 'Password field is required'
#             }, status=status.HTTP_400_BAD_REQUEST)
            
#         user = authenticate(username=email, password=password)

#         # user = authenticate(email=email, password=password)

#         u = User.objects.get(username=user)
#         se = UserProfile.objects.filter(user_id=u.id)
#         print(se)

#         # print(user)

#         if not user:
#             return Response({
#                 'detail': 'Invalid Credentials'
#             }, status=status.HTTP_401_UNAUTHORIZED)

#         token, created = Token.objects.get_or_create(user=user)
#         serializer = UserInfoSerializer(user)

#         return Response({
#             'user': serializer.data,
#             'token': token.key
#         })
#     except:
#         return Response({
#             'detail': 'Oops, something went wrong-1!'
#         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def register_user(request):
    try:
        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     user = serializer.save()

        #     token = Token.objects.get(user=user)
        #     return Response({
        #         'user': UserInfoSerializer(user).data,
        #         'token': token.key
        #     }, status=status.HTTP_201_CREATED)
        # return Response({
        #     'details': serializer.errors
        # }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'detail': 'Oops, something went wrong!1'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return Response({
            'detail': 'Oops, something went wrong!1'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        request.user.auth_token.delete()
        return Response({
            'detail': 'You have been logged out!'
        },status=status.HTTP_200_OK)
    except:
        return Response({
            'detail': 'Oops, something went wrong!'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)