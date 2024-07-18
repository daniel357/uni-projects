# Generated by Django 4.1.7 on 2023-04-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_delete_operatingflights'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='flight',
            name='base_flight_departu_a4eaf3_idx',
        ),
        migrations.AddIndex(
            model_name='flight',
            index=models.Index(fields=['departure_airport', 'arrival_airport', 'operating_aircraft'], name='base_flight_departu_cb7dc6_idx'),
        ),
    ]