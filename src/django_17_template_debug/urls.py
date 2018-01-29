from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_17_template_debug.views.home', name='home'),
    url(r'^contact/', include('contact.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
