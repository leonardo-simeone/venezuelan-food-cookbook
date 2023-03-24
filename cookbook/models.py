from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='recipe_creator')
    title = models.CharField(max_length=200, unique=True)
    short_description = models.CharField(max_length=150, null=True, blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    food_image = CloudinaryField('image', default='default-image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title + ' by ' + self.creator.username


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment made by ' + self.name + ' on ' + self.recipe.title
