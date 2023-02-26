
from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name = 'demo'),
    path('result/', views.result, name = "result"),
    path('blah/', views.blah, name = 'blah')
]
