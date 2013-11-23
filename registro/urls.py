from django.conf.urls import patterns, url

from registro import views

urlpatterns = patterns('',
	url(r'^detalle/$', views.ParticipanteDetailView.as_view(),\
		name='detalle'),
    url(r'^registrar/$', views.ParticipanteCreate.as_view(), name='registrar'),
    url(r'^modificar/$', views.ParticipanteUpdate.as_view(),\
    	name='modificar'),
    url(r'^success_create/$', views.success_create_view,\
    	name='success_create'),    
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
)