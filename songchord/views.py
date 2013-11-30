from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from songchord.models import Song,Chord


# Create your views here.
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def index(request):
	return render(request,'songchord/index.html')

def search_form(request):
	return render(request,'songchord/search_form.html')
	
def search_result(request):
	if 'chord' in request.GET and request.GET['chord']: 
		chord = request.GET['chord']
		songs = Song.objects.filter(chord__name__exact= chord)
		return render(request,'songchord/search_result.html',
		{'query': chord, 'songs':songs})
	

def song_page(request,song_id):
	songname=Song.objects.get(id=song_id)
	chords = Song.objects.get(id=song_id).chord_set.all()
	return render(request,'songchord/song_page.html',
	{'chords':chords,'songname':songname
	})
	
	#template = loader.get_template('songchord/search_result/song_page.html')
    #context = RequestContext(request, {
    #'chords': chords,
    #})






	

