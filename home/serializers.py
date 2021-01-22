from rest_framework import routers,serializers,viewsets
from django.contrib.auth.hashers import make_password
from .models import *

from django.core.mail import send_mail
from django.conf import settings

from django.http import JsonResponse


class CommissionaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commissionaire
        fields = ('__all__')
        extra_kwargs = {'user': {'required':False}}

class UserCommissionaireSerializer(serializers.ModelSerializer):
    commissionaire = CommissionaireSerializer(required=True)
    class Meta:
        model = User
        fields = ('username','email','password','commissionaire','first_name','last_name')

    def create(self, validate_data):
        insert = User.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            password = make_password(validate_data['password']),
            first_name = validate_data['first_name'],
            last_name = validate_data['last_name']
        )
        commissionaire_data = validate_data.pop('commissionaire')   
        commissionaire = Commissionaire.objects.create(
            user = insert,
            phone =commissionaire_data['phone'],
            location =commissionaire_data['location']
        )
        
        return insert
    
            # fields=('__all__')

class HouseuploadedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houseuploaded
        depth = 1
        fields = ('__all__')
        

