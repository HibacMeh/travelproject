from django.urls import path
from . import views

urlpatterns = [
   
   path('cred', views.cred, name = "cred"),
   path('login', views.login, name = "login"),
   path('logout', views.logout, name= 'logout')
]