# Generated by Django 4.0.1 on 2022-01-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0019_rename_features_propertyfeature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='features',
        ),
        migrations.AddField(
            model_name='propertyfeature',
            name='property',
            field=models.ManyToManyField(to='properties.Property', verbose_name='features'),
        ),
    ]
