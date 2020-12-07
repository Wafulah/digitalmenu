from django.shortcuts import render

from .models import Meal,Price,Drinks


def index(request):
    latest_meal_list = Meal.objects.order_by('-pub_date')[:5]
    latest_drinks_list = Drinks.objects.order_by('-pub_date')[:5]
    price_list = Price
    context = {'latest_meal_list': latest_meal_list,
               'price_list': price_list,
               'latest_drinks_list': latest_drinks_list }
    return render(request, 'menu/index.html', context)


# Leave the rest of the views (detail, results, vote) unchanged