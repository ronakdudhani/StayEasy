# Generated by Django 4.2 on 2024-12-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('category', models.CharField(choices=[('beach', 'Beach'), ('mountain', 'Mountain'), ('cabin', 'Cabin'), ('apartment', 'Apartment')], max_length=50)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability_start', models.DateField()),
                ('availability_end', models.DateField()),
                ('image', models.ImageField(upload_to='property_images/')),
            ],
        ),
    ]
