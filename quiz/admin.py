from django.contrib import admin
from .models import Newspaper, NewspaperQuiz, QuizInstance
from .forms import QuizInstanceForm


# Register your models here.
admin.site.register(Newspaper)
admin.site.register(NewspaperQuiz)


class QuizInstanceAdmin(admin.ModelAdmin):
    form = QuizInstanceForm
    list_display = ('__str__', 'display_newspaper_name',
                    'score', 'display_max_score')


admin.site.register(QuizInstance, QuizInstanceAdmin)
