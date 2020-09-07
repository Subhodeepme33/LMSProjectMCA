from django.urls import path,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home),
    path('register',views.register),
    path('login',views.login),
   
]
