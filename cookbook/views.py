from django.shortcuts import render, redirect
from .models import *


def recipes(request):

    recipes_list = Recipe.objects.all()

    context = {'recipes_list': recipes_list}

    return render(request, 'index.html', context)


def recipeUnit(request, pk):

    recipe_object = Recipe.objects.get(id=pk)
    comments = recipe_object.comments.all()

    context = {'recipe_object': recipe_object, 'comments': comments}

    return render(request, 'recipe.html', context)
