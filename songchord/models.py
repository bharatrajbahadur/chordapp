from django.db import models

# Create your models here.
class Song(models.Model):
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)

	def __unicode__ (self):
		return self.title


class Chord(models.Model):
	name= models.CharField(max_length=20)
	songs= models.ManyToManyField(Song)

	def __unicode__(self):
		return self.name



#>>> Song.objects.filter(chord__name__exact='D').filter(chord__name__exact='B')
#[<Song: Jester Dance>]
#>>> Song.objects.filter(chord__name__exact='D').exclude(chord__name__exact='B')
#[<Song: OneChord>]
#>>> 