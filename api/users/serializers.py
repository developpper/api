from rest_framework import serializers
# from .models import User
from django.contrib.auth.models import User

from account.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], username=validated_data['username'], password=validated_data['password'])
        return user
        
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['email', 'username']
        fields = ['username']
    

class UserProfileSerializer(serializers.Serializer):
    class Meta:
        model = UserProfile
        fields =  ['base_company_id']