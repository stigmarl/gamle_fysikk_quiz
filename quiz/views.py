from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
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


class NewspaperCreate(CreateView):
    model = Newspaper
    fields = '__all__'


class NewspaperUpdate(UpdateView):
    model = Newspaper
    fields = '__all__'


class NewspaperDelete(DeleteView):
    model = Newspaper
    success_url = reverse_lazy('newspapers')
