from django.conf.urls import url, path
from .import views
from djano.contrib.auth.views import login, signup
from accounts.forms import LoginForm

urlpatterns = [
    url(r'^$', views.home),
    url(r'^registroauto/$', views.registro),
    path('login/', login, {'template_name':'registration/login.html','authentication_form':LoginForm}, name='login')
]
