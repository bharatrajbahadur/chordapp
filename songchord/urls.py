from django.conf.urls import patterns, url
from songchord import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^search/', views.search_form, name='search'),
	url(r'^search_result/', views.search_result, name='search_result'),
	url(r'^(?P<song_id>\d+)', views.song_page, name='song_page'),
	url(r'^(?P<artist_name>\w+\s\w+)', views.artist_page, name='artist_page'),
	#url(r'^song_page/',views.song_page,name='song_page'),
	#url(r'^display_meta/',view.display_meta,name='display_meta'),
	

)