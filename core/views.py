from django.shortcuts import render
from .forms import RestaurantForm
from core.models import Restaurant, Sale, Rating, StaffRestaurant
from django.db.models import Sum,Prefetch
from django.utils import timezone

def index(request):
    jobs = StaffRestaurant.objects.prefetch_related('restaurant','staff')

    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)
    return render(request, 'index.html')



"""
    ratings = Rating.objects.only('rating','restaurant__name').select_related('restaurant')
    context = {'ratings' : ratings}

    restaurants = Restaurant.objects.filter(name__istartswith = 'c').prefetch_related('ratings','sales')
    context = {'restaurants' : restaurants}
"""