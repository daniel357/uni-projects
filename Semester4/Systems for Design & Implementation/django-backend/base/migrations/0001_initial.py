# Generated by Django 4.1.7 on 2023-03-18 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('headquarters', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('establishedDate', models.DateField()),
                ('revenue', models.IntegerField()),
                ('numEmployees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('timezone', models.CharField(max_length=100)),
                ('elevation', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('noGates', models.IntegerField()),
                ('noTerminals', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('booking_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('tickets', models.ManyToManyField(related_name='passengers', to='base.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('status', models.CharField(default=None, max_length=255)),
                ('price', models.FloatField(default=None)),
                ('seats_available', models.IntegerField(default=None)),
                ('arrival_airport', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='base.airport')),
                ('departure_airport', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='base.airport')),
                ('tickets', models.ManyToManyField(related_name='flights', to='base.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('maxSpeed', models.IntegerField()),
                ('seatingCapacity', models.IntegerField()),
                ('fuel_capacity', models.IntegerField()),
                ('wing_span', models.IntegerField()),
                ('length', models.IntegerField()),
                ('no_engines', models.IntegerField()),
                ('airline_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.airline')),
                ('flights', models.ManyToManyField(to='base.flight')),
            ],
        ),
    ]