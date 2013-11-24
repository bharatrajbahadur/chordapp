from django.contrib import admin
from songchord.models import Song
from songchord.models import Chord

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Artist information', {'fields': ['artist'], 'classes': ['collapse']}),
    ]
admin.site.register(Song,SongAdmin)
admin.site.register(Chord)