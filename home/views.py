from django.shortcuts import render
from django. http import HttpResponse
from .models import*
from .serializers import*
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import requests

#email

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def welcome(request):
    return HttpResponse('welcom home')


@csrf_exempt
def commissionaire(request):
    if request.method == 'GET':
        comm = User.objects.all().select_related('commissionaire')
        serializer = UserCommissionaireSerializer(comm, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserCommissionaireSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'sucessfull saved'}, status=201)
        return JsonResponse(serializer.errors, status=400)    
    

@csrf_exempt
def houseuploade(request):
    
    pass