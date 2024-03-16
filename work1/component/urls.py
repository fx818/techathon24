from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('index',views.index,name = 'index'),
    path('home',views.home,name = 'home'),
    path('application',views.application,name = 'application'),
    path('allrequests',views.allrequests,name = 'allrequests'),
    path('register',views.register,name = 'register')
]