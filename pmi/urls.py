from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registro/', include('registro.urls', namespace="registro")),
    url(r'^admin/', include(admin.site.urls)),

)
