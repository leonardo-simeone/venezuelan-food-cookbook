from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField


class Recipe(models.Model):

    """
    The Recipe class inherits from django.db models, it contains a tuple
    which defines the recipe tags used in the tags field. It also has all
    the fields used for the model. This model is used to hold the information
    pertaining to recipe objects attributes. There are two particular
    relationships in the model, the creator field has a One to Many
    relationship with User since one user can create many recipes and
    the likes field has a M2M relationship with User since many users
    can like many recipes. This model has a meta class to determine the
    descending order of the recipe objects and two helper methods,
    one to count the number of likes and one to represent the objects
    with a custom string.
    """

    RECIPE_TAGS = (('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Supper', 'Supper'), ('Dessert', 'Dessert'), ('Drink', 'Drink'),)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='recipe_creator')
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    short_description = models.CharField(max_length=100, null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    instructions = HTMLField(null=False, blank=False)
    food_image = CloudinaryField('image', default='default-image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = MultiSelectField(max_length=120, choices=RECIPE_TAGS, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-created']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' by ' + self.creator.username


class Comment(models.Model):

    """
    The Comment class inherits from django.db models, it contains
    the information pertaining to comment objects attributes.
    There is one particular relationship in the model, the recipe field
    has a One to Many relationship with Recipe since one recipe
    can have many comments. This model has a meta class to determine
    the ascending order of the comment objects and one helper method
    to represent the objects with a custom string.
    """

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment made by ' + self.name + ' on ' + self.recipe.title
