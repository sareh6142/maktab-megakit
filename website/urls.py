from django.contrib import admin
from django.urls import path,include
from .views import home_view,contact_view,about_view,licenses_view

urlpatterns = [
    
    path('',home_view,name='home'),
    path('contact/',contact_view,name = 'contact'),
    path('about/',about_view, name = 'about'),
    path('licences',licenses_view, name = 'licenses'),
]
