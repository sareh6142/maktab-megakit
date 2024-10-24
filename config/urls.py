"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import customhandler404
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib.auth import views as authViews
from.views import maintenance



sitemaps = {
    "static": StaticViewSitemap,
    "blog":BlogSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('maintenance/', maintenance, name='maintenance'),

    path('blog/',include('blog.urls')),
    path('reset_password/',authViews.PasswordResetView.as_view(),name= 'reset_password'),
    path('reset_password_sent/',authViews.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',authViews.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',authViews.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('robots.txt', include('robots.urls')),
    path('captcha/', include('captcha.urls')),
    path('accounts/',include('accounts.urls'))
]+ debug_toolbar_urls()
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
