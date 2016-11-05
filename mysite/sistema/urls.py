from django.conf.urls import url
from sistema.views import *

urlpatterns = [
    url(r'^dados/$', dados, name='dados'),
    url(r'^login$', do_login, name='login'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^cadastro$', cadastro, name='cadastro'),
    
 
    ]