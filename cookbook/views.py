from django.shortcuts import render, redirect
from .models import *


def recipes(request):

    recipes_list = Recipe.objects.all()

    context = {'recipes_list': recipes_list}

    return render(request, 'index.html', context)
