from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower

def run():

    chinese = Restaurant.TypeChoices.CHINESE

    sales = Sale.objects.filter(restaurant__restaurant_type = chinese)
    print(sales)
    pprint(connection.queries)


'''   

    sales  = Sale.objects.order_by('-datetime')
    print(sales)
    pprint(connection.queries)
    restaurants = Restaurant.objects.exclude(restaurant_type__in = [chinese, indian,mexican])
sales = Sale.objects.filter(income__range = (50,60))
    print(sales)
    indian = Restaurant.TypeChoices.INDIAN
    mexican = Restaurant.TypeChoices.MEXICAN
    check_types = [chinese, indian,mexican]
    restaurants = Restaurant.objects.filter(restaurant_type__in = check_types)
    print(restaurants)

 restaurants = Restaurant.objects.filter(restaurant_type = chinese, name__startswith='C')
    print(restaurants)
    restaurant = Restaurant.objects.filter(name ="Pizzeria 1")
    print(restaurant.count())

    # restaurant = Restaurant.objects.get(name ="Pizzeria 1")
    # print(restaurant)
    # print(restaurant.count())
    # print(restaurant.get())
    # pprint(connection.queries)
    Restaurant.objects.all().delete()

print(restaurant.update(
        date_opened = timezone.now() - timezone.timedelta(days=365),
        website = "https://test.com"
    ))
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


# Restaurant.objects.all() fetch all the objects form the database
# Restaurant.objects.create() to create data
# Restaurant.objects.count() count number of rows in database
# Restaurant.objects.last() return last record
# Restaurant.objects.first() return first record
# Restaurant.objects.filter() take the condition and return based on matched condition
# Restaurant.objects.exclude() it is opposite of filter function