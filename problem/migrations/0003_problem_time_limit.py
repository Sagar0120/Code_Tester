# Generated by Django 3.2.6 on 2021-09-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_auto_20210905_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='time_limit',
            field=models.IntegerField(default=1000),
        ),
    ]
