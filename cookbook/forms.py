from django.forms import ModelForm
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'short_description', 'ingredients', 'instructions', 'food_image']


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
