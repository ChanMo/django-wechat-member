from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^auth/$', views.auth, name='auth'),
]
