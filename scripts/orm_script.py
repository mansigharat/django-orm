from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating = Rating(user = user, restaurant = restaurant, rating=4)
    rating.full_clean()
    rating.save()


# Restaurant.objects.all() #fetch all the objects form the database
# Restaurant.objects.create() to create data
# Restaurant.objects.count() count number of rows in database
# Restaurant.objects.last() return last record
# Restaurant.objects.first() return first record
# Restaurant.objects.filter() take the condition and return based on matched condition
# Restaurant.objects.exclude() it is opposite of filter function