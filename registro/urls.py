from django.conf.urls import patterns, url

from registro import views

urlpatterns = patterns('',
    url(r'^registrar/$', views.ParticipanteCreate.as_view(), name='registrar'),
    url(r'^(?P<pk>\d+)/modificar/$', views.ParticipanteUpdate.as_view(),\
    	name='modificar'),
)