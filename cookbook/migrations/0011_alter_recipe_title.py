# Generated by Django 3.2.18 on 2023-04-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0010_alter_recipe_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
