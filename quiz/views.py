from django.views import generic
from django.shortcuts import render
from .models import Newspaper, NewspaperQuiz, QuizInstance


def index(request):
    """View function for home page of the site."""

    # Generate counts of some of the main objects.
    num_newspapers = Newspaper.objects.all().count()

    context = {
        'num_newspapers': num_newspapers
    }

    return render(request, 'index.html', context=context)


class QuizInstanceListView(generic.ListView):
    model = QuizInstance


class NewspaperListView(generic.ListView):
    model = Newspaper


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperQuizListView(generic.ListView):
    model = NewspaperQuiz


class NewspaperQuizDetailView(generic.DetailView):
    model = NewspaperQuiz
