from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def register(request):
   

   if request.method=='POST':
      

     First_name=request.POST.get('First_name')
     username=request.POST.get('username')
     email=request.POST.get('email')
     Password=request.POST.get('Password')
     


     x=User.objects.create_user(first_name=First_name,username=username,email=email,password=Password)
     x.save;
     messages.info(request,'user created')

     return redirect('login')   
   else:
     return render(request,'register.html')


def login(request):
   if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')

      user=auth.authenticate(username=username,password=password)

      if user is not None:
         auth.login(request, user)

         return redirect("/")

      else:
         messages.info(request,'invalid crendentials !')
         return redirect('login')
   else:
     return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")


def home(request):
      return render(request, 'home.html')
