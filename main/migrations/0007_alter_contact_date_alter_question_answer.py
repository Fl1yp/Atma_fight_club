# Generated by Django 5.0.7 on 2024-08-19 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_contact_date_alter_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 19, 7, 34, 5, 355945, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=300, verbose_name='Ответ'),
        ),
    ]
