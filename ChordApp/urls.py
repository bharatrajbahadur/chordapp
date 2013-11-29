from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChordApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^songchord/',include('songchord.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^song_page/',include('songchord.urls')),
)
