# Generated by Django 3.2 on 2022-03-12 21:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Booking_approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
    ]
