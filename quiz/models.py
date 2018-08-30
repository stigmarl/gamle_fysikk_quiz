from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

from datetime import date

# Create your models here.


class Newspaper(models.Model):

    name = models.CharField(
        max_length=100, blank=False, null=True, help_text="Navnet på avisen")

    class Meta:
        verbose_name = "Avis"
        verbose_name_plural = "Aviser"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('newspaper-detail', args=[str(self.id)])


class NewspaperQuiz(models.Model):

    newspaper = models.ForeignKey(
        Newspaper, on_delete=models.CASCADE, help_text="Avisen")
    max_score = models.IntegerField(help_text="Øverste poenggrense",
                                    validators=[MaxValueValidator(60)], blank=False, default=20)

    class Meta:
        verbose_name = "Avisquis"
        verbose_name_plural = "Avisquizer"

    def __str__(self):
        return "{0}-quiz".format(self.newspaper.name)

    def get_absolute_url(self):
        return reverse('news-quiz-detail', args=[str(self.id)])


class QuizInstance(models.Model):

    newspaper_quiz = models.ForeignKey(NewspaperQuiz, on_delete=models.CASCADE)
    completed_date = models.DateField(default=date.today)
    score = models.IntegerField(default=0, verbose_name="Poeng")

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizer"

    def display_newspaper_name(self):
        return self.newspaper_quiz.newspaper.name

    display_newspaper_name.short_description = "Avis"

    def display_max_score(self):
        return self.newspaper_quiz.max_score

    display_max_score.short_description = "Poenggrense"

    def __str__(self):
        return "{0} ({1})".format(self.newspaper_quiz, self.completed_date)
