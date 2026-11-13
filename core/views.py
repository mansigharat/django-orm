from django.shortcuts import render
from .forms import RestaurantForm
from core.models import Restaurant, Sale, Rating

def index(request):
    restaurants = Restaurant.objects.filter(name__istartswith = 'c').prefetch_related('ratings','sales')
    context = {'restaurants' : restaurants}
    return render(request, 'index.html', context)