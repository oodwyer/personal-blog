# Generated by Django 2.2.7 on 2019-11-14 03:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.CharField(default='Description', max_length=250),
        ),
    ]
