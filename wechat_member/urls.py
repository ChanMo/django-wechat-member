from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wx_auth/$', views.WxAuth.as_view(), name='auth'),
]
