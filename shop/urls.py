from django.contrib import admin
from django.urls import path, include
from shop.views import main, contacts

urlpatterns = [
    path('', main, name='main_page'),
    path('contacts/', contacts, name='contacts'),
]
