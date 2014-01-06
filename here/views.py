from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from here.models import Event, AttendeeForm, Attendee
from ucd import searchdir

def index(request, nomatch=False):
    events_now = Event.events.get_happening_now() #get all the events that are happening now
    context = {'events_now': events_now, 'nomatch': nomatch}
    return render(request, 'here/index.html', context)

def validate(request):
	if request.method == 'POST':

		form = AttendeeForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			result_name = searchdir(email)
			event = request.POST['eventslist']
			
			if len(result_name) == 1: #success!
				context = {'email': email, 'result_name': result_name[0], 'event': event}
				print "hooray!!!!!"
				newAttendee = Attendee(name=result_name[0], email=email)
				newAttendee.save()
				eventEntry = Event.objects.get(name=event)
				print ("event: %s attendee: %s", (eventEntry, newAttendee))
				eventEntry.attendees.add(newAttendee)
				print eventEntry.attendees.all()
				return render(request, 'here/thanks.html', context)
			
			elif len(result_name) == 0: #no match found
				return index(request, True) #raise a 
			
			else: # multiple matches found
				context = {'email': email, 'result_name': result_name[0], 'event': event}
				return render(request, 'here/select.html', context)
		else:
			return HttpResponse("something went wrong!")

	#for testing purposes
	return HttpResponse("oops, something went wrong. sorry!")

def thanks(request):
	if request.method == 'POST':
		return HttpResponse("yay!")




