from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models import Count, Avg, Min, Max, CharField, Value, Sum, F, Q, Case, When, Value
from django.db.models.functions import Upper, Lower, Length, Concat
import random
from django.db.models.functions import Coalesce

def run():
    restaurants = Restaurant.objects.annotate(
        avg = Avg('ratings__rating'),
        num_ratings = Count('ratings__pk')
    )

    print(restaurants.values('avg', 'num_ratings'))
    restaurants = restaurants.annotate(
    rating_bucket=Case(
        When(avg__gt=3.5, then=Value('Highly Rated')),
        When(avg__range=(2.5, 3.5), then=Value('Average Rated')),
        When(avg__lt=2.5, then=Value('Bad Rated')),
        default=Value('Not Rated'),
        output_field=CharField()
    )
)

    print(restaurants.filter(rating_bucket='Highly Rated'))
    # print(connection.query)
''' 
    italian = Restaurant.TypeChoices.ITALIAN

    r = Restaurant.objects.annotate(
        is_italian = Case(
            When(restaurant_type = italian, then = True),
            default = False
        )
    )

    print(
        r.filter(is_italian = True)
    )
    print(
        Restaurant.objects.filter(capacity__isnull = False).order_by('-capacity').values('capacity')
    )
    # restaurant = Restaurant.objects.first()
    # restaurant2 = Restaurant.objects.last()

    # restaurant.capacity = 10

    # restaurant2.capacity = 20
    profited = Q(income__gt = F('expenditure'))
    name_has_number = Q(restaurant__name__regex = r"[0-9]+")

    sales = Sale.objects.filter(name_has_number & profited).distinct()
    print(sales)

    for sale in sales:
        if sale.income <= sale.expenditure:
            print(sale.restaurant.name)
    
    recently_opened = ~Q(date_opened__gt = timezone.now() - timezone.timedelta(days = 40))
    restaurants = Restaurant.objects.filter(recently_opened)
    it = Restaurant.TypeChoices.ITALIAN
    mex = Restaurant.TypeChoices.MEXICAN
    r = Restaurant.objects.filter(
        Q(restaurant_type=it)| Q(restaurant_type = mex)
    )
    print(r)

    # sales = Sale.objects.annotate(
    #     profit= F('income') - F('expenditure')
    # ).order_by('-profit')
    # print(sales.first().profit)
    # for sale in sales:
    #     sale.expenditure = random.uniform(5,100)

    # Sale.objects.bulk_update(sales, ['expenditure'])
    Rating.objects.update(rating = F('rating')/2)

    rating = Rating.objects.filter(rating = 3).first()
    rating.rating = F('rating') + 1
    rating.save() 
    # restaurant = Restaurant.objects.annotate(total_sales = Sum('sales__income')).order_by('total_sales')
    # print(restaurant)
    # restaurants = Restaurant.objects.values_list('latitude', flat = True)
    # print(restaurants)
    # print(Rating.objects.filter(restaurant__name__startswith='c').aggregate(avg = Avg('rating')))

    restaurants = Restaurant.objects.annotate(total_sales = Sum('sales__income')).values(
        'name', 'total_sales'
    )
    print([r['total_sales'] for r in restaurants])

concatenation = Concat(
        'name',Value(' [Rating: '),Avg('ratings__rating'), Value(']'),
    output_field = CharField()
    )
    restaurants = Restaurant.objects.annotate(message = concatenation)

    for r in restaurants:
        print(r.message)
restaurants = Restaurant.objects.annotate(len_name=Length('name')).filter(
        len_name__gt = 10
    )
    print(restaurants.values('name','len_name'))
    one_month_ago = timezone.now() - timezone.timedelta(days = 31)
    sales = Sale.objects.filter(datetime__gte = one_month_ago)
    print(sales.aggregate(
        avg = Avg('income'),
        min = Min('income'),
        max = Max('income'),
        sum = Sum('income'),
        ))
    # IT = Restaurant.TypeChoices.ITALIAN

    restaurants = Restaurant.objects.values(name_upper  = Upper('name'))[:3]
    print(restaurants)
 restaurants = Restaurant.objects.values('name','date_opened').first()
    print(restaurants) 
    staff , created = Staff.objects.get_or_create(name='Jonh deo')
    staff.restaurants.set(
        Restaurant.objects.all()[:10], 
        through_defaults = {'salary':random.randint(35_000,85_000)}
    )
    staff.restaurants.clear()

    restaurant = Restaurant.objects.first()
    staff.restaurants.add(restaurant, through_defaults={'salary': 50_000})
    staff,created = Staff.objects.get_or_create(name = "John Wick")
    # print(staff.restaurants.all())
    # staff.restaurants.add(Restaurant.objects.first())
    india = staff.restaurants.filter(restaurant_type = Restaurant.TypeChoices.INDIAN)
    print(india)
    chinese = Restaurant.TypeChoices.CHINESE

    sales = Sale.objects.filter(restaurant__restaurant_type = chinese)
    print(sales)
    pprint(connection.queries)
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
    print(connection.queries)

    Restaurant.objects.all() fetch all the objects form the database
    Restaurant.objects.create() to create data
    Restaurant.objects.count() count number of rows in database
    Restaurant.objects.last() return last record
    Restaurant.objects.first() return first record
    Restaurant.objects.filter() take the condition and return based on matched condition
    Restaurant.objects.exclude() it is opposite of filter function



Two commonly used methods are aggregate () and annotate (). 
aggregate () summarizes data across the entire queryset (e.g., total, average, count). 
annotate () computes and adds calculated values for each individual object in the queryset.
     
'''

