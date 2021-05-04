from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [ 
        path('create-user/', views.UserCreate.as_view(), name='account-create'),
]