from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import imageupload
from .models import contactus
from .models import ims
# Create your views here.


def home(request):
      return render(request, 'home.html')


def login(request):
      return render(request, 'login.html')

def kullu(request):
      return render(request, 'kullu.html')

def chamba(request):
      return render(request, 'chamba.html')

def temple(request):
      return render(request, 'temple.html')

def khajjiar(request):
      return render(request, 'khajjiar.html')

def kinnaur(request):
      return render(request, 'kinnaur.html')

def ims(request):
 if request.method=='POST':
   return redirect("/")
 else:
   return render(request,'ims.html')

def contact(request):
 if request.method=='POST':
   name=request.POST.get('name')
   message=request.POST.get('message')

   ins=contactus(name=name,message=message)
   ins.save()
   return redirect("/")
 else:
   return render(request,'contact.html')

def kangra(request):
      return render(request, 'kangra.html')

def dharmshala(request):
      return render(request, 'dharmshala.html')

def fort(request):
      return render(request, 'fort.html')

def shimla(request):
      return render(request, 'shimla.html')

def gallery(request):
     posts=imageupload.objects.all()
     return render(request, 'gallery.html', {'posts':posts})
