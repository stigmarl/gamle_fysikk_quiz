# Generated by Django 2.1 on 2018-08-10 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_max_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='completed_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
