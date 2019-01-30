from django.conf.urls import url
from django.urls import re_path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path(r'^login/$', authapp.login, name='login'),
    re_path(r'^logout/$', authapp.logout, name='logout'),
    re_path(r'^register/$', authapp.register, name='register'),
    re_path(r'^edit/$', authapp.edit, name='edit'),
    re_path(r'^verify/(?P<email>.+)/(?P<active_key>\w+)/$', authapp.verify, name='verify'),
    
]

    