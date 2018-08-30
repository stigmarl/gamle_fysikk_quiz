from django.urls import path
from quiz import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newspapers/', views.NewspaperListView.as_view(), name='newspapers'),
    path('newspapers/<int:pk>', views.NewspaperDetailView.as_view(),
         name='newspaper-detail'),
    path('newsquiz/', views.NewspaperQuizListView.as_view(), name='news-quizs'),
    path('newsquiz/<int:pk>', views.NewspaperQuizDetailView.as_view(),
         name='news-quiz-detail')
]
