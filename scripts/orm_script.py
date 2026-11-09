from core.models import Restaurant,Rating
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():
    # restaurant = Restaurant.objects.first()
    # print(restaurant.name)
    # restaurant.name = 'Indian Hotel'
    # restaurant.save()

    # print(Rating.objects.exclude(rating__gte= 3))
    # print(Rating.objects.filter(rating = 5))

    rating = Rating.objects.first()
    print(rating.restaurant)
    pprint(connection.queries)

# Restaurant.objects.all() #fetch all the objects form the database
# Restaurant.objects.create() to create data
# Restaurant.objects.count() count number of rows in database
# Restaurant.objects.last() return last record
# Restaurant.objects.first() return first record
# Restaurant.objects.filter() take the condition and return based on matched condition
# Restaurant.objects.exclude() it is opposite of filter function