from django.shortcuts import render, redirect
from .models import *
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# --------------------------------------------------------------------------
# Register View


def registerView(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

# --------------------------------------------------------------------------
# Login view


def loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('recipes')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

# --------------------------------------------------------------------------
# Display recipes view


def logoutView(request):
    logout(request)
    return redirect('recipes')

# --------------------------------------------------------------------------
# Display recipes view


def recipes(request):

    recipes_list = Recipe.objects.all()

    context = {'recipes_list': recipes_list}

    return render(request, 'index.html', context)

# --------------------------------------------------------------------------
# Display recipe Unit view


def recipeUnit(request, pk):

    recipe_object = Recipe.objects.get(id=pk)
    comments = recipe_object.comments.all()

    context = {'recipe_object': recipe_object, 'comments': comments}

    return render(request, 'recipe.html', context)
