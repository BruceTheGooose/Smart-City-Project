##Import files
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout
##Patterns
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    #url(r'^login/$', login, {'template_name': 'personal/login.html'}),
    url(r'templates/personal/login.html$', views.login, name = 'login'),
    url(r'templates/personal/register.html$', views.register, name = 'register'),
    url(r'^logout/$', logout, {'template_name': 'personal/logout.html'}),
    #url(r'^register/$', views.register, name='register'),
    url(r'^map.html$', views.map, name = 'map'),
    url(r'templates/personal/profile.html$', views.profile, name = 'profile'),
    url(r'templates/personal/admin.html$', views.admin, name = 'admin'),
    url(r'templates/personal/index.html$', views.home, name = 'home'),
    ]
