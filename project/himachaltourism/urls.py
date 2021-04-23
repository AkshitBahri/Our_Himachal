from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('kullu',views.kullu,name='kullu'),
    path('chamba',views.chamba,name='chamba'),
    path('temple' ,views.temple,name='temple'),
    path('khajjiar' ,views.khajjiar,name='khajjiar'),
    path('kinnaur' ,views.kinnaur,name='kinnaur'),
    path('ims' ,views.ims,name='ims'),
    path('gallery' ,views.gallery,name='gallery'),
    path('dharmshala' ,views.dharmshala,name='dharmshala'),
    path('kangra' ,views.kangra,name='kangra'),
    path('fort' ,views.fort,name='fort'),
    path('contact' ,views.contact,name='contact'),
    path('shimla' ,views.shimla,name='shimla'),


    ]
