from django.urls import path
from .import views

urlpatterns = [
    path('', views.SendMail, name='index')
]
