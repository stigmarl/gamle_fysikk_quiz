from django import forms
from .models import QuizInstance


class QuizInstanceForm(forms.ModelForm):
    class Meta:
        model = QuizInstance
        fields = '__all__'

    def clean_score(self):
        cleaned_data = self.cleaned_data
        max_score = cleaned_data.get('newspaper_quiz').max_score
        score = cleaned_data.get('score')
        if score > max_score:
            raise forms.ValidationError(
                'Score exceeds maximum score ({0})'.format(max_score))
        return score
