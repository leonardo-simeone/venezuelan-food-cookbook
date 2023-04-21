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

    """
    The RecipeForm class inherits from django.forms ModelForm,
    it contains a variable that defines the form tags field
    which will use RECIPE_TAGS as its choices and CheckboxSelectMultiple
    as its widget. It also has a meta class to set the model and
    fields to use in the form.
    """

    tags = forms.MultipleChoiceField(
        required=False,
        choices=RECIPE_TAGS,
        widget=forms.widgets.CheckboxSelectMultiple()
    )

    class Meta:
        model = Recipe
        fields = ['title', 'short_description', 'ingredients', 'instructions', 'tags', 'food_image']


class NewUserForm(UserCreationForm):

    """
    The NewUserForm class inherits from
    django.contrib.auth.forms UserCreationForm,
    it contains a meta class to set the model
    and fields to use in the form.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):

    """
    The CommentForm class inherits from
    django.forms ModelForm, it contains
    a meta class to set the model and fields
    to use in the form.
    """

    class Meta:
        model = Comment
        fields = ['body']
