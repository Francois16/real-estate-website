# Generated by Django 4.0.1 on 2022-01-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_alter_property_options_property_baths_property_beds'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='Levies',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='property',
            name='erf_size',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='floor_size',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='garage',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='has_garden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='is_pet_friendly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='parking',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='rates_and_taxes',
            field=models.SmallIntegerField(null=True),
        ),
    ]
