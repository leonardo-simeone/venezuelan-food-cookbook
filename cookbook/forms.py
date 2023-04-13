from django.forms import ModelForm
from .models import Recipe, Comment
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

RECIPE_TAGS = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Supper', 'Supper'),
    ('Dessert', 'Dessert'),
    ('Drink', 'Drink'),
)


class RecipeForm(ModelForm):
    tags = forms.MultipleChoiceField(
        required=False,
        choices=RECIPE_TAGS,
        widget=forms.widgets.CheckboxSelectMultiple()
    )

    class Meta:
        model = Recipe
        fields = ['title', 'short_description', 'ingredients', 'instructions', 'tags', 'food_image']


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
