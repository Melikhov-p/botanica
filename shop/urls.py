from django.contrib import admin
from django.urls import path, include
from shop.views import main, contacts, about_us, admin_logout

urlpatterns = [
    path('logout/', admin_logout, name='admin_logout'),
    path('', main, name='main_page'),
    path('shop/', main, name='main_page'),
    path('shop/<str:category_slug>/', main, name='product_list_by_category'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about_us, name='about_us'),
]
