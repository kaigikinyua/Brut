# Generated by Django 2.1.7 on 2020-07-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200712_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_class',
            field=models.CharField(default='Saloon', max_length=50),
        ),
    ]
