from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_creator', null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)
    short_description = models.CharField(max_length=150, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    food_image = CloudinaryField('image', default='default-image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title + ' by ' + self.creator.username
