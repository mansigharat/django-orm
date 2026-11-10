from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():
    restaurant = Restaurant.objects.filter(name__startswith = 'P')
    print(restaurant)

    print(restaurant.update(
        date_opened = timezone.now() - timezone.timedelta(days=365)
    ))
    pprint(connection.queries)


'''   
    restaurant = Restaurant()
    restaurant.name = 'My Indian 2'
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    restaurant.latitude = 50.2
    restaurant.longitude = 50.9
    restaurant.save()

    restaurant = Restaurant.objects.first()
    print(restaurant.name)

    restaurant.name = 'New Restaurant Name'
    restaurant.save(update_fields =['name']) # used to update only specific field
    print(connection.queries)'''


# Restaurant.objects.all() #fetch all the objects form the database
# Restaurant.objects.create() to create data
# Restaurant.objects.count() count number of rows in database
# Restaurant.objects.last() return last record
# Restaurant.objects.first() return first record
# Restaurant.objects.filter() take the condition and return based on matched condition
# Restaurant.objects.exclude() it is opposite of filter function