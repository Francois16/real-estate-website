# Generated by Django 4.0.1 on 2022-01-20 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0016_remove_property_has_garden_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyfeatures',
            old_name='property',
            new_name='prop',
        ),
    ]