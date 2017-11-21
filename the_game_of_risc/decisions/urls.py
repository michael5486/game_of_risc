from django.conf.urls import url

from . import views

app_name = 'decisions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<adjudication_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^random/$', views.random, name='random')

]