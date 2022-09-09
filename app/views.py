
from cmath import e
import email
from email import message
from email.mime import image
from urllib import request
from django.shortcuts import render,HttpResponse,redirect
from .models import happy, Complaints, sad
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as user_Auth
from django.contrib.auth.models import User



import pyrebase
firebaseConfig= {
  'apiKey': "AIzaSyB9IAFOI6NUwcx9HALoEmBrLPehuD4INhA",
  'authDomain': "hello-fe480.firebaseapp.com",
  'databaseURL': "https://hello-fe480-default-rtdb.firebaseio.com",
  'projectId': "hello-fe480",
  'storageBucket': "hello-fe480.appspot.com",
  'messagingSenderId': "868252179136",
  'appId': "1:868252179136:web:77e1243c4bb5307e21ab25",
  'measurementId': "G-47FMCJ5LRV"}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()  
  
def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user =auth.create_user_with_email_and_password(email=email, password=password)
        return render(request, "login.html")
    return render(request,"signup.html")


def login(request):
    if request.method==['POST']:
        email=request.POST["email"]
        password=request.POST["password"]
        login=auth.sign_in_with_email_and_password(email,password)
        if (email==email or password==password):
            print("login sucessfully")    
        else:
            print("useranem and password") 
    else:
        return render(request,'signup.html')  
 


# from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method=="POST":
        your_Name=request.POST.get('your_name')
        Email=request.POST.get('email')
        Message=request.POST.get('message')
        image=request.FILES.get('image')
        # Timestamp=request.POST.get('Timestamp')
        print(image)
        you=happy(your_name=your_Name,email=Email,message=Message,image=image)
        you.save()
        # return redirect('ok')
    return render(request,'contact.html')
def reg(request):
    if request.method=="POST":
        your_Name=request.POST.get('your_name')
        Email=request.POST.get('email')
        Message=request.POST.get('message')
        image=request.FILES.get('image')
        # Timestamp=request.POST.get('Timestamp')
        print(image)
        you=sad(your_name=your_Name,email=Email,message=Message,image=image)
        you.save()
        # return redirect('ok')
    return render(request,'reg.html')

        
        # send_mail(
        #     your_Name,
        #     Email,
        #     ['shubham@gmail.com'],
        #     Message,
        # )

    

# def signup(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user =auth.create_user_with_email_and_password(email=email, password=password)
#         user.save()
#         return render(request, "login.html")
#     return render(request,"signup.html")

def login(request):
    if request.method == 'POST':
        username =  request.POST['username']
        email =  request.POST['email']
        password =  request.POST['password']
        
        print(username, password)
        x=authenticate(username=username,password=password,email=email)
        if x is not  None:
            return render(request,"contact.html")
        

        else:
            return redirect("login")
    return render(request,"login.html")

def add(request):
    if request.method == 'POST':
        Your_Name =  request.POST.get('your_name')
        Email =  request.POST.get('email')
        Message =  request.POST.get('message')
        image =  request.FILES.get('image')
        why = happy(your_name=Your_Name, email=Email, message=Message,image=image)
        why .save()
    return render(request,'add.html')            

    # return render(request, 'login.html')    
def hike(request):
    return render(request,'hike.html')
def ok(request):
    return HttpResponse('working')
def about(request):
    return render(request,'about.html')
def run(request):
    x = happy.objects.all()
    context = {'x':x}
def go(request):
    no = Complaints.objects.all()
    context = {'no':no}
    return render(request, 'go.html',context)   
def profile(request):
    x = happy.objects.all()
    context = {'x':x}
    return render(request, 'profile.html',context) 

def complaint(request):
    if request.method == 'POST':
        name =  request.POST.get('name')
        title =  request.POST.get('title')
        age =  request.POST.get('age')
        gender =  request.POST.get('gender')
        discription =  request.POST.get('discription')
        image =  request.FILES.get('image')
        why = Complaints(name=name, title=title, age=age,gender=gender,discription=discription,image=image)
        why.save()
    return render(request,'complaint.html')  

def admlogin(request):
    if request.method == 'POST':
        username =  request.POST['username']
        password =  request.POST['password']
        
        print(username, password)
        x=authenticate(username=username,password=password)
        
        if x is not  None:
            user_Auth(request, x)
            return redirect("go")
        else:
            return redirect("admlogin")
    return render(request,"admlogin.html")
    



