from django.contrib import admin
from django.urls import path,include
from .views import blog_view,blog_single

app_name = 'blog'

urlpatterns = [
   path('',blog_view,name = 'blog'),
   path('<int:pk>/',blog_single, name ='blog_single')
]
