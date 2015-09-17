import datetime

from django.db import models
from django.utils import timezone





#DATABASE NOT NORMALIZED, DON'T WANT IT TO BE


#call this something else, could screw up the internals
class User(models.Model):
    createdAt = models.DateTimeField('user creation date')
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=6)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    totalMatches = models.IntegerField()
    missedMatches = models.IntegerField()
    def __unicode__(self):
      return self.firstName + ' ' + self.lastName



    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # def __unicode__(self):              # __str__ on Python 3
    #     return self.question_text
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField()
    def __unicode__(self):
      return self.name




class Match(models.Model):
    user1 = models.CharField(max_length=100)
    user2 = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    date = models.DateTimeField()
    showedUp = models.BooleanField()
    def __unicode__(self):
      return self.user1 + ' + ' + self.user2 + ' @ ' + self.location





