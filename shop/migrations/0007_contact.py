# Generated by Django 3.1 on 2020-09-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200904_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('desc', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
