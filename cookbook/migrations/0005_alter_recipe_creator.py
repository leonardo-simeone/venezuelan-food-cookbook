# Generated by Django 3.2.18 on 2023-03-24 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0004_alter_recipe_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]