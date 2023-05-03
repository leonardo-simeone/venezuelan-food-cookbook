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

    """
    The registerView function takes request as an argument
    and instantiates a form by calling NewUserForm.
    It then runs the logic to create a new user and log it
    in if there is a POST request, otherwise it loads an empty
    NewUserForm.
    """

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

    """
    The loginView function takes request as an argument.
    If there is a POST request it sets username and password,
    it then runs the logic to authenticate and login a user
    by using the authenticate and login methods,
    if the information submitted is incorrect, a message will be
    shown indicating so, otherwise it loads an empty login form.
    """

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

    """
    The logoutView function takes request as an argument.
    Then the logout method is called to log out the user,
    a message is shown to indicate the user it has been logged out
    and the user is redirected home.
    """

    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('recipes')

# --------------------------------------------------------------------------
# Display recipes view


def recipes(request):

    """
    The recipes function takes request as an argument.
    Then recipes_list is defined equal to all the
    recipe objects, and the index page is rendered with
    recipes_list as its context, if there are more than
    three objects then paginator is used.
    """

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

    """
    The recipeUnit function takes request and
    primary key as arguments. It then defines the
    recipe_object by calling the get method, it
    also defines tags, comments and total_likes
    using the recipe_object and comment_form
    using CommentForm and liked is set to false
    by default. The context is created and passed
    to the recipe template to be rendered.
    If a comment is made via POST request,
    the logic sets the name equal to username,
    saves the comment, displays a message to
    indicate the user that comment was successfully
    added and redirects the user to recipeUnit.
    """

    recipe_object = Recipe.objects.get(id=pk)
    tags = recipe_object.tags
    comments = recipe_object.comments.all()
    comment_form = CommentForm()
    total_likes = recipe_object.total_likes()
    liked = False

    if recipe_object.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'recipe_object': recipe_object, 'tags': tags, 'comments': comments,
        'comment_form': comment_form, 'total_likes': total_likes,
        'liked': liked
        }

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe_object
            comment.save()
            messages.success(
                request, 'Your comment has been successfully added'
                )
            return redirect(recipeUnit, pk)
    else:
        comment_form = CommentForm()

    return render(request, 'recipe.html', context)

# --------------------------------------------------------------------------
# Create new recipe view


def createRecipe(request):

    """
    The createRecipe function takes request as an argument
    and instantiates a form by calling RecipeForm.
    If there is a POST request it runs the logic to create
    a new recipe object, show a message to the user to confirm
    recipe creation and redirect user home, otherwise it loads an empty
    RecipeForm.
    """

    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            messages.success(
                request, 'You have successfully created ' + form.instance.title
                )
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'recipe-form.html', context)

# --------------------------------------------------------------------------
# Update recipe view


def updateRecipe(request, pk):

    """
    The updateRecipe function takes request and
    primary key as arguments. It defines recipe_object by calling the get
    method, it instantiates a form by calling RecipeForm and passing the
    recipe_object as its instance to prefill the form.
    If there is a POST request it runs the logic to save
    the changes made to recipe_object, show a message to the user to confirm
    recipe update and redirect user to recipeUnit, otherwise
    it loads a prefilled RecipeForm.
    """

    recipe_object = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe_object)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe_object)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully updated ' + form.instance.title
                )
            return redirect(recipeUnit, pk)

    context = {'form': form}
    return render(request, 'update-recipe.html', context)

# --------------------------------------------------------------------------
# Delete recipe view


def deleteRecipe(request, pk):

    """
    The deleteRecipe function takes request and
    primary key as arguments. It defines recipe by calling the get
    method. If there is a POST request it runs the logic to delete
    recipe, show a message to the user to confirm
    recipe deletion and redirect user home, otherwise
    it loads the delete template with recipe as its context.
    """

    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        messages.success(
            request, 'You have successfully deleted ' + recipe.title
            )
        return redirect('recipes')

    return render(request, 'delete.html', {'recipe': recipe})

# --------------------------------------------------------------------------
# About Us view


def aboutUs(request):

    """
    The aboutUs function takes request as an argument
    and it renders the about-us template.
    """

    return render(request, 'about-us.html')

# --------------------------------------------------------------------------
# Gallery view


def gallery(request):

    """
    The gallery function takes request as an argument.
    Then recipes_list is defined equal to all the
    recipe objects and gallery template is rendered
    with recipes_list as its context.
    """

    recipes_list = Recipe.objects.all()

    context = {'recipes_list': recipes_list}

    return render(request, 'gallery.html', context)

# --------------------------------------------------------------------------
# Like view


def likeRecipe(request, pk):

    """
    The likeRecipe function takes request and
    primary key as arguments. It defines recipe_object by calling the
    get_object_or_404 method and sets liked to False as default.
    If there is a POST request and a 'like' associated to that recipe
    and that user exists, then it will remove the like from the recipe
    and change the liked to False, but if there is a POST request
    and a 'like' associated to that recipe and that user does not exists,
    then it will add the like to the recipe and change the liked to True,
    a message will be shown to the user in both cases to indicate that
    they have liked or unliked the recipe, and they will be redirected
    to recipeUnit.
    """

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
