# Generated by Django 2.2.7 on 2019-11-14 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191114_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
