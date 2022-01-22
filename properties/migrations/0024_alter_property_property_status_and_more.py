# Generated by Django 4.0.1 on 2022-01-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0023_alter_property_created_at_alter_property_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_status',
            field=models.CharField(choices=[('S', 'For Sale'), ('R', 'To Rent'), ('F', 'Forclosure'), ('A', 'Auction')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('H', 'House'), ('AP', 'Apartment / Flat'), ('TH', 'Townhouse'), ('P', 'Vacant Land / Plot'), ('F', 'Farm'), ('C', 'Commercial Property'), ('I', 'Industrial Property')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='province',
            field=models.CharField(choices=[('FS', 'Free State'), ('G', 'Gauteng'), ('KZN', 'KwaZulu-Natal'), ('MPG', 'Mpumalanga'), ('NC', 'Northern Cape'), ('NW', 'North West'), ('EC', 'Eastern Cape'), ('WC', 'Western Cape')], max_length=4, null=True),
        ),
    ]
