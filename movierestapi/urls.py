from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^movieapp/', include('movierestapi.movieapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)