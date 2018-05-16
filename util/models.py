# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

STATUS = (
    ('I', 'Initial'),
    ('P','Pending'),
    ('R', 'Resolved'),
)
TYPE = (
    ('B','Bug'),
    ('S', 'Suggestion'),
)

PRIORITY = (
    ('N','None'),
    ('H', 'Hight'),
    ('M', 'Medium'),
    ('L', 'Low'),
)
class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length = 50, null = True, blank = True)
    created_by = models.CharField(max_length = 100, blank = True)

    class Meta:
        abstract = True


class ConnectionSetting(models.Model):

    name = models.CharField(max_length=100)
    server = models.CharField(max_length=50)
    database = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)


class FeedBack(BaseEntity):

    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=50,choices= STATUS)
    feedback_type = models.CharField(max_length=50,choices= TYPE)
    priority = models.CharField(max_length=50,choices= PRIORITY)
 
    def __unicode__(self):     
        return self.title

    def __str__(self):
        return self.title

