from django.urls import path
from . import views

urlpatterns = [
    path('user/register', views.register),
    path('user/login', views.login),
    path('user/idCheck', views.id_check),
    path('user/nickCheck', views.nickname_check),
]
# python .\manage.py runserver