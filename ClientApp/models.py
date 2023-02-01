from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    #สร้าง File ฐานขอมูลดังนี้
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name +" " +str(self.age)


class Stat_user(models.Model):


    tel = models.CharField(max_length=10,default='081xxxxxxx')
    slot = models.CharField(max_length=5,null=True,blank=True)
    game = models.CharField(max_length=5,null=True,blank=True)
    huay = models.CharField(max_length=5,null=True,blank=True)
    muay = models.CharField(max_length=5,null=True,blank=True)
    ball = models.CharField(max_length=5,null=True,blank=True)
    bacara = models.CharField(max_length=10,null=True,blank=True)
    sms = models.CharField(max_length=3,null=True,blank=True)
    sex = models.CharField(max_length=3,null=True,blank=True)
    age = models.CharField(max_length=3,null=True,blank=True)
    date = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return str(self.tel)



