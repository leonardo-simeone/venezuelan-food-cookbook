# Generated by Django 3.2.18 on 2023-04-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0009_auto_20230407_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='short_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
