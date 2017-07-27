from __future__ import unicode_literals

from django.db import models

# Create your models here.

#for general contact inquiries on our site
class Contact(models.Model):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    subject = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=300, null=True, blank=True)
    filing_type = models.CharField(max_length=300, null=True, blank=True)
    business_type = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField(max_length=3000)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Message from: " + str(self.email)