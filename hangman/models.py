from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):   # table class inherits 
    name = models.CharField(max_length=30)
    score = models.IntegerField(default=0)

    def __unicode__(self):  # __str__ on Python 3
        return "%s: %d" %(self.name, self.score)


##class Score(models.Model):
##    user = models.ForeignKey(User)
##    score = models.IntegerField(default=0)
##
##    def __unicode__(self):
##        return self.score
