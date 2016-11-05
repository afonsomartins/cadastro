from django.conf.urls import url,include
from django.contrib import admin
from sistema.views import registroForm

urlpatterns = [
    url(r'^', include('sistema.urls')),
    url(r'^admin/', admin.site.urls),
    
 
    
]
