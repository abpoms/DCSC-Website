from django.http import HttpResponseRedirect
from django import forms
from django.db.utils import IntegrityError
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.contrib import messages

from dcsc_website.models import NewsletterEmails


def index(request):
    context = {}
    if request.method == 'POST':
        try:
            email = forms.EmailField().clean(request.POST['email'])
            news_email = NewsletterEmails(email=email)
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
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'dcsc_website/index.html', {})
    else:
        return render(request, 'dcsc_website/index.html', context)
