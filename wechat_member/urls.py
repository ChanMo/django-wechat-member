from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_member/$', views.get_member, name='get_member'),
    url(r'^clear_session/$', views.clear_session, name='clear_session'),
]
