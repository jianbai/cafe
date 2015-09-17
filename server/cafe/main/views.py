from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from users.models import User
from django.utils import timezone

import requests
import math

# once we start using celery, alot of these tasks
# will be done using a queue (not createUser)



def createUser(request):
  print(request.GET)
  #this is how we get queryArgs
  fn = request.GET['fn']
  ln = request.GET['ln']
  age = request.GET['age']
  sex = request.GET['sex']
  email = request.GET['email']
  password = request.GET['password']
  u = User(createdAt=timezone.now(), firstName=fn, lastName=ln, a=age, s=sex, email=email, password=password, totalMatches=0, missedMatches=0)
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

  #run the search algorithm for the specified user

  #find the midpoint between the two users' latlons
  m = midpoint(x1, y1, x2, y2)

  #use this midpoint and some specified radius for the Yelp query

  #r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
  r =  requests.get('https://google.com')
  print('wooo'+ str(r.status_code))
  print(r.cookies)

  response = JsonResponse({'matches': 'none'})
  return response


def reviewMatch(request):


  #add the rating to the proper match


  response = JsonResponse({'thanks': 'for reviewing'})
  return response








def midpoint(x1, y1, x2, y2):
#Input values as degrees

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






