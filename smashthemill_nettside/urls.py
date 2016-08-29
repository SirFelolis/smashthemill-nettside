from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from templatetest import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    url(r'^templatetest/', include('templatetest.urls')),
    url(r'^admin/', admin.site.urls),
]
