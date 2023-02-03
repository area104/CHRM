from django.shortcuts import render,redirect
from django.http import HttpResponse
from ClientApp.models import *
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime 
from django.contrib import messages

# Create your views here.
def index(request):

    names = {"name":"ภูมิพัฒน์","age":[40,60]} #ส่งแบบเป็น dict ไปเลย
    lname = Person.objects.all() # ส่งเป็นตัวแปร แล้วไปทำเป็น dict อีกครั้งใน return render
    age25 = Person.objects.filter(age__gt = 25 )

   
    return render (request,"index.html",{"name":names,"lname":lname,"age":age25})



def about (request):

    person = Person.objects.all() # เป็นการดึงข้อมูลทั้งหมด
    fperson = Person.objects.filter(age__gt=25 ) #กรองเอาเฉพาะข้อมูลไปแสดง
    return render(request,"about.html",{"persons":person,"fperson":fperson})
             

def form (request):

    # แสดงข้อมูล block Left1
    if request.method == "POST":


        #รับข้อมูลมาจาก HTML

        name = request.POST["name"]
        age = request.POST["age"]
        print(name,age)


         #บันทึกข้อมูล

        person = Person.objects.create(
            age = age,
            name = name,
            )
        person.save()

        messages.success(request,"สำเร็จ")
        return redirect('about-page')    
            
    else:        
        return render(request,"form.html")

    
def edit (request,id):

    if request.method == "POST":

        #ดึงข้อมูล id มา model
        person = Person.objects.get(id=id)

        name = request.POST["name"]#ดึงข้อมูล name มาจาก POST
        age = request.POST["age"]
        person.name = name
        person.age = age
        person.save()

        messages.success(request,"อัพเดด")
        return redirect('about-page') 


    else:
        person_data = Person.objects.get(id=id) # เข้าไปที่ person getเอาข้อมูล มาด้วยid = id ที่ส่งมา เก็บไว้ในตัวแปล person

        return render (request,"edit.html",{"person":person_data}) #ส่งข้อมูลไปที่ edit.html เรียกด้วย person เก็บข้อมูล person_data เอาไว้


def delete(request,id):
    
    person = Person.objects.get(id=id)
    person.delete()

    messages.success(request,"ลบข้อมูล")
    return redirect('about-page') 



def profile(request):

    person = Person.objects.all()

    return render(request,'profile.html',{"person":person})



def register (request):
    if request.method == 'POST' :  

    #เก็บข้อมูลมาจาก HTML ก่อนดังนี้
        data = request.POST.copy()
        username = data.get("email")
        password = data.get('password')
        repassword = data.get('password')
        first_name = data.get('first_name')

        
        #เก็บข้อมูลลง Database
        user = User.objects.create_user(
            username = username,
            password= password,
            first_name = first_name,
            email=username,
        )

        #เซฟข้อมูล
        user.save()
        return redirect('/')
    else:
        return render(request,'register.html') 


def show_user (request):
    user = User.objects.all()
    return render(request,'show_user.html/',{"users":user})


def show_cust (request):
    user = Stat_user.objects.all()
    return render(request,'show_cust.html/',{'users':user})    

def regis_cust (request):

    if request.method == "POST":
        data = request.POST.copy()
        tel = data.get("tel")
        slot = data.get("slot")
        game = data.get("game")
        huay = data.get("huay")
        muay = data.get("muay")
        ball = data.get("ball")
        bacara = data.get("bacara")
        sms = data.get("sms")
        sex = data.get("sex")
        age = data.get("age")

        newrecord = Stat_user()
        newrecord.tel = tel
        newrecord.slot = slot
        newrecord.tel = tel
        newrecord.game = game
        newrecord.huay = huay
        newrecord.muay = muay
        newrecord.ball = ball
        newrecord.bacara = bacara
        newrecord.sms = sms
        newrecord.sex = sex
        newrecord.age = tel

        newrecord.save()
        return redirect("/show_cust")
    else:
        show = Stat_user.objects.all()
        return render(request,"regis_cust.html",{"show":show})

def edit_cust (request,tel):

    if request.method == "POST":

        #ดึงข้อมูล person_id มา model
        tel = Stat_user.objects.get(tel=tel)

        

        messages.success(request,"อัพเดด")
        return redirect('regis_cust-page') 


    else:
        tel = Stat_user.objects.get(tel=tel) # เข้าไปที่ person getเอาข้อมูล มาด้วยid = person_id ที่ส่งมา เก็บไว้ในตัวแปล person

        return render (request,"edit_cust.html",{"tel":tel}) #ส่งข้อมูลไปที่ edit.html เรียกด้วย person เก็บข้อมูล person_data เอาไว้ 
