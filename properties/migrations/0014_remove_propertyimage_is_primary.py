# Generated by Django 4.0.1 on 2022-01-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_alter_propertyimage_property'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyimage',
            name='is_primary',
        ),
    ]
