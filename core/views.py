from django.shortcuts import render
from .forms import RestaurantForm
from core.models import Restaurant, Sale, Rating
from django.db.models import Sum,Prefetch
from django.utils import timezone

def index(request):
    month_ago = timezone.now() - timezone.timedelta(days =30)
    monthly_sales = Prefetch(
        'sales',
        queryset = Sale.objects.filter(datetime__gte = month_ago)
    )
    r = Restaurant.objects.prefetch_related('ratings',monthly_sales).filter(ratings__rating = 5) 
    print(r)
    return render(request, 'index.html')



"""

    ratings = Rating.objects.only('rating','restaurant__name').select_related('restaurant')
    context = {'ratings' : ratings}

    restaurants = Restaurant.objects.filter(name__istartswith = 'c').prefetch_related('ratings','sales')
    context = {'restaurants' : restaurants}
"""