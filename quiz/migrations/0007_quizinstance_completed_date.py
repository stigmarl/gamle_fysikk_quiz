# Generated by Django 2.1 on 2018-08-10 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20180810_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizinstance',
            name='completed_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
