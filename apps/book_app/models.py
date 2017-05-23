# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    #in real practice, use datetime.datetime.strptime() to convert string into datetime
    #instead of an auto generated NOW value
    published_date = models.DateTimeField() 
    category = models.CharField(max_length=50)
    in_print = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return ("id: "+str(self.id)+", title: "+self.title+", author: "+self.author+", published_date: "+str(self.published_date)+", category: "+self.category+", in_print: "+str(self.in_print))