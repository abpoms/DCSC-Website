from django.http import HttpResponseRedirect
from django import forms
from django.db import transaction
from django.db.utils import IntegrityError
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail

from dcsc_website.models import NewsletterEmail, Carousel, FailedSignup
from schedule.models.events import Event
from schedule.utils import EventListManager
from smtplib import SMTPException

import itertools


def index(request):
    if request.method == 'POST':
        try:
            email = forms.EmailField().clean(request.POST['email'])
            news_email = NewsletterEmail(email=email)
            news_email.save()
        except KeyError:
            messages.error(request, 'Uh oh')
        except ValidationError:
            messages.error(request, 'Invalid email format!')
        except IntegrityError:
            messages.error(request, 'Email already signed up!')
        else:
            messages.success(
                request,
                'Woo ho, your email was submitted succesfully!')
            # Add user to the mailing list
            try:
                send_mail('invite',
                          'invite csclub %s' % email,
                          'officer@daviscsclub.org',
                          ['sympa@ucdavis.edu'],
                          fail_silently=False)
            except SMTPException:
                FailedSignup(failed_email=email).save()
        finally:
            response = HttpResponseRedirect(reverse('index'))
            return response
    eventManager = EventListManager(Event.objects.all())
    context = {
        'upcoming_occurences': itertools.islice(
            eventManager.occurrences_after(timezone.now()),
            3),
        'carousel': Carousel.objects.all()
    }
    response = render(request, 'dcsc_website/index.html', context)
    return response
