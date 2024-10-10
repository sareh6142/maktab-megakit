from django.contrib import admin
from django.urls import path,include
from .views import *
app_name= 'website'

urlpatterns = [
    
    path('',home_view,name='home'),
    path('contact/',contact_view,name = 'contact'),
    path('about/',about_view, name = 'about'),
    path('project/',project_view, name = 'project'),
    path('service/',service_view, name = 'service'),
    path('newsletter', newsletter_view , name = 'newsletter'),

]
