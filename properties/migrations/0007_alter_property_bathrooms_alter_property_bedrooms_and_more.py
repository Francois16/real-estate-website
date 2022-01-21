# Generated by Django 4.0.1 on 2022-01-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_property_suburb_alter_property_erf_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='erf_size',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='floor_size',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='garage',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='parking',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
