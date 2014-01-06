from django.contrib import admin

# Register your models here.
from here.models import Event, Attendee

class EventAdmin(admin.ModelAdmin):
	filter_horizontal = ('attendees',)

admin.site.register(Event, EventAdmin)

class AttendeeAdmin(admin.ModelAdmin): #HORRIBLE. NEED TO CHANGE somehow.
	fields = ['name', 'email']
	list_display= ('name','events_attended')

admin.site.register(Attendee, AttendeeAdmin)