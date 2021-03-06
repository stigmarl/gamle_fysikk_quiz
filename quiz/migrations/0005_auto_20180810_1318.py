# Generated by Django 2.1 on 2018-08-10 13:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20180810_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewspaperQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_points', models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(60)], verbose_name='Øverste poenggrense')),
            ],
            options={
                'verbose_name': 'Avisquis',
                'verbose_name_plural': 'Avisquizer',
            },
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='newspaper',
        ),
        migrations.AlterModelOptions(
            name='newspaper',
            options={'verbose_name': 'Avis', 'verbose_name_plural': 'Aviser'},
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Navnet på avisen'),
        ),
        migrations.AlterField(
            model_name='quizinstance',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.NewspaperQuiz'),
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.AddField(
            model_name='newspaperquiz',
            name='newspaper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Newspaper', verbose_name='Avisen'),
        ),
    ]
