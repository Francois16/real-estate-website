# Generated by Django 4.0.1 on 2022-01-19 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_rename_image_propertyimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='properties.property'),
        ),
    ]
