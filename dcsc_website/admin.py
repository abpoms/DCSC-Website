from django.contrib import admin
from dcsc_website.models import NewsletterEmail, Carousel


admin.site.register([NewsletterEmail, Carousel])
