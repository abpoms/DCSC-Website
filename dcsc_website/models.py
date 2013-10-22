from django.db import models


class NewsletterEmail(models.Model):
    email = models.EmailField(max_length=254, unique=True, blank=False)

    def __unicode__(self):
        return self.email


class FailedSignup(models.Model):
    failed_email = models.ForeignKey(NewsletterEmail)

    def __unicode__(self):
        return self.failed_email


class Carousel(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='carousel')

    def __unicode__(self):
        return self.title
