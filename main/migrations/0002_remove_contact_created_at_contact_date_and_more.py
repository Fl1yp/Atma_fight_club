# Generated by Django 5.0.7 on 2024-07-31 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_at',
        ),
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 10, 43, 9, 361906, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=12, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=15, verbose_name='Номер'),
        ),
    ]
