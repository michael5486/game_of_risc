from django.conf.urls import url

from . import views

app_name = 'decisions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<adjudication_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<adjudication_id>[0-9]+)/$', views.result, name='result'),
    url(r'^new/$', views.decision_new, name='decision_new')

]