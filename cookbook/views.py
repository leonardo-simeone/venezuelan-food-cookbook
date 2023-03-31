from django.shortcuts import render, redirect
from .models import *
from .forms import NewUserForm, RecipeForm, CommentForm
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
    tags = recipe_object.tags
    comments = recipe_object.comments.all()
    comment_form = CommentForm()

    context = {'recipe_object': recipe_object, 'tags': tags, 'comments': comments, 'comment_form': comment_form}

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe_object
            comment.save()
            return redirect(recipeUnit, pk)
    else:
        comment_form = CommentForm()

    return render(request, 'recipe.html', context)

# --------------------------------------------------------------------------
# Create new recipe view


def createRecipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'recipe-form.html', context)

# --------------------------------------------------------------------------
# Update recipe view


def updateRecipe(request, pk):
    recipe_object = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe_object)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe_object)
        if form.is_valid():
            form.save()
            return redirect(recipeUnit, pk)

    context = {'form': form}
    return render(request, 'update-recipe.html', context)

# --------------------------------------------------------------------------
# Delete recipe view


def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')

    return render(request, 'delete.html', {'recipe': recipe})

# --------------------------------------------------------------------------

