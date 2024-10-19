from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authViews

app_name = 'accounts'
urlpatterns = [
    
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name ='logout'),
    path('signup/', views.signup_view,name ='signup'),
    


 

]
