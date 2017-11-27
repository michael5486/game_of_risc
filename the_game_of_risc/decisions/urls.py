from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'decisions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<adjudication_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^random/$', views.random, name='random'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),

]