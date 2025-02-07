from django.contrib import admin
from .models import Location, Event
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Location) 

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'category', 'created')
    search_fields = ['title']
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
    
# Register your models here.
