from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone

from django.forms import ModelForm

class Attendee(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	def __unicode__(self):
		return self.name
	def events_attended(self):
		return "\n".join("%s - %s" % (e.name, e.date) for e in self.event_set.all())
	events_attended.short_description = "Events Attended"

class HereEventManager(models.Model): #return list of events that are happening now
	def get_happening_now(self):
		now = datetime.now() #get current time
		events_now = []
		for event in Event.objects.all():
			if (event.happening_now()):
				events_now.append(event)
		return events_now

class Event(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateField()
	time_start = models.TimeField('start')
	time_end = models.TimeField('end')
	location = models.CharField(max_length=100)
	desc = models.TextField()
	image = models.ImageField(upload_to='events-images', blank=True)
	attendees = models.ManyToManyField(Attendee, blank=True)
	objects = models.Manager()
	events = HereEventManager()

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name

	def happening_now(self): #returns true if now is in between time_start and time_end
		now = datetime.now() - timedelta(hours=8) #get current time, hardcoded to UTC-8
		# an event is happening now if:
		# event start time is after now and event end time is before now and event date is today
		if ((self.time_start <= now.time()) and (self.time_end >= now.time()) and (now.date() == self.date)):
			return True
		else:
			return False
	def attendee_list(self): #the list of all the attendees
		return "\n".join("%s - %s" % (a.name, a.email) for a in self.attendees.all())

class AttendeeForm(ModelForm):
	class Meta:
		model = Attendee
		fields = ['email']


