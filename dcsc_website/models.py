from django.db import models


class NewsletterEmails(models.Model):
    email = models.EmailField(max_length=254, unique=True, blank=False)
