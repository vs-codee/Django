# Generated by Django 3.1 on 2020-09-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200914_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zipcode',
            field=models.CharField(max_length=100),
        ),
    ]
