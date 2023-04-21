from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import NewUserForm, RecipeForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            new_user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1'),
            )
            login(request, new_user)
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
            messages.success(request, 'Welcome back ' + user.username)
            return redirect('recipes')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

# --------------------------------------------------------------------------
# Logout view


def logoutView(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('recipes')

# --------------------------------------------------------------------------
# Display recipes view


def recipes(request):

    recipes_list = Recipe.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(recipes_list, 3)

    try:
        recipes_list = paginator.page(page)
    except PageNotAnInteger:
        recipes_list = paginator.page(1)
    except EmptyPage:
        recipes_list = paginator.page(paginator.num_pages)

    context = {'recipes_list': recipes_list}

    return render(request, 'index.html', context)

# --------------------------------------------------------------------------
# Display recipe Unit view


def recipeUnit(request, pk):

    recipe_object = Recipe.objects.get(id=pk)
    tags = recipe_object.tags
    comments = recipe_object.comments.all()
    comment_form = CommentForm()
    total_likes = recipe_object.total_likes()
    liked = False

    if recipe_object.likes.filter(id=request.user.id).exists():
        liked = True

    context = {'recipe_object': recipe_object, 'tags': tags, 'comments': comments, 'comment_form': comment_form, 'total_likes': total_likes, 'liked': liked}

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe_object
            comment.save()
            messages.success(request, 'Your comment has been successfully added')
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
            messages.success(request, 'You have successfully created ' + form.instance.title)
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
            messages.success(request, 'You have successfully updated ' + form.instance.title)
            return redirect(recipeUnit, pk)

    context = {'form': form}
    return render(request, 'update-recipe.html', context)

# --------------------------------------------------------------------------
# Delete recipe view


def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'You have successfully deleted ' + recipe.title)
        return redirect('recipes')

    return render(request, 'delete.html', {'recipe': recipe})

# --------------------------------------------------------------------------
# About Us view


def aboutUs(request):

    return render(request, 'about-us.html')

# --------------------------------------------------------------------------
# Gallery view


def gallery(request):

    recipes_list = Recipe.objects.all()

    context = {'recipes_list': recipes_list}

    return render(request, 'gallery.html', context)

# --------------------------------------------------------------------------
# Like view


def likeRecipe(request, pk):
    recipe_object = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    liked = False

    if recipe_object.likes.filter(id=request.user.id).exists():
        recipe_object.likes.remove(request.user)
        liked = False
        messages.success(request, 'You have UNLIKED ' + recipe_object.title)
    else:
        recipe_object.likes.add(request.user)
        liked = True
        messages.success(request, 'You have LIKED ' + recipe_object.title)

    return redirect(recipeUnit, pk)
