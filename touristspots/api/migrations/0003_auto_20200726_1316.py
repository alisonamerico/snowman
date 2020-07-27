# Generated by Django 3.0.8 on 2020-07-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200725_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='category',
            field=models.CharField(choices=[('PARK', 'Park'), ('MUSEUM', 'Museum'), ('THEATER', 'Theater'), ('MONUMENT', 'Monument')], max_length=50),
        ),
    ]