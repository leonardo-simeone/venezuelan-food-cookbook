# Generated by Django 3.2.18 on 2023-04-12 12:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0013_alter_recipe_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(related_name='recipe_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
