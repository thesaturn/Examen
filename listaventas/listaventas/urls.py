"""listaventas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url, include
from app.views import auto_vista_test, auto_lista, contacto, login, home, home2
from django.contrib.auth import views as auth_views
from app import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('registro/', auto_vista_test),
    path('lista/', auto_lista),
    path('contacto/', contacto),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', core_views.signup, name='signup'),
    path('home2/', home2),

]
