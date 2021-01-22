from django.db import models
from django.contrib.auth.models import User
# Create your models here.



#user account 
class Commissionaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

#uploaded house   
class Houseuploaded(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    housetype = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    pricenegotiable = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    bathroom = models.CharField(max_length=255)
    bedroom = models.CharField(max_length=255)
    parkingcar = models.CharField(max_length=255)
    plotsize = models.CharField(max_length=255)
    photo1 = models.FileField()
    photo2 = models.FileField()
    photo3 = models.FileField()
    photo4 = models.FileField()
    photo5 = models.FileField()
    photo6 = models.FileField()
    province = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    
