from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone

from main.models import User

import requests
import math


# once we start using celery, alot of these tasks
# will be done using a queue (not createUser)



def createUser(request):



  #this is how we get queryArgs
  fn = request.GET['fn']
  ln = request.GET['ln']
  age = request.GET['age']
  sex = request.GET['sex']
  email = request.GET['e']
  password = request.GET['p']



  # TODO - check to make sure email/username isn't taken before creating


  u = User(createdAt=timezone.now(), inPool=False, signedIn=True, hasReviewed=True, firstName=fn, lastName=ln, age=age, sex=sex, email=email, password=password, totalMatches=0, missedMatches=0)

  u.save()

  response = JsonResponse({'possibly': 'created user'})

  return response




def signIn(request):
  #check password and sign em in
  response = JsonResponse({'signin': 'false'})
  return response



def signOut(request):
  #sign em out
  response = JsonResponse({'signout': 'false'})
  return response


def signUp(request):
  #this puts the user into the match pool for that day
  response = JsonResponse({'woo':'woo'})
  return response


def findMatch(request):

  #TODO - check to make sure they reviewed their last match

  #TODO - run the search algorithm for the specified user

  #find the midpoint between the two users' latlons
  #m = midpoint(x1, y1, x2, y2)

  #TODO - use this midpoint and some specified radius for the Yelp query

  #r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
  r =  requests.get('https://google.com')
  print('wooo'+ str(r.status_code))
  print(r.cookies)

  #TODO - create match in the db, (create location if need to?)

  response = JsonResponse({'matches': 'none'})
  return response



def reviewMatch(request):
  #TODO - add the rating to the proper match
  response = JsonResponse({'thanks': 'for reviewing'})
  return response



#Input values as degrees
def midpoint(x1, y1, x2, y2):
#Convert to radians
  lat1 = math.radians(x1)
  lon1 = math.radians(x2)
  lat2 = math.radians(y1)
  lon2 = math.radians(y2)

  bx = math.cos(lat2) * math.cos(lon2 - lon1)
  by = math.cos(lat2) * math.sin(lon2 - lon1)
  lat3 = math.atan2(math.sin(lat1) + math.sin(lat2), \
         math.sqrt((math.cos(lat1) + bx) * (math.cos(lat1) \
         + bx) + by**2))
  lon3 = lon1 + math.atan2(by, math.cos(lat1) + Bx)

  return [round(math.degrees(lat3), 2), round(math.degrees(lon3), 2)]






