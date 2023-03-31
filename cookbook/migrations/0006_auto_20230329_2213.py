# Generated by Django 3.2.18 on 2023-03-29 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_alter_recipe_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, to='cookbook.Tag'),
        ),
    ]
