from django.urls import path
from quiz import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newspapers/', views.NewspaperListView.as_view(), name='newspapers'),
    path('newspapers/add/', views.NewspaperCreate.as_view(), name='newspaper-add'),
    path('newspapers/<int:pk>', views.NewspaperDetailView.as_view(),
         name='newspaper-detail'),
    path('newspaper/<int:pk>/update/',
         views.NewspaperUpdate.as_view(), name='newspaper-update'),
    path('newspapers/<int:pk>/delete/',
         views.NewspaperDelete.as_view(), name='newspaper-delete'),
    path('newsquiz/', views.NewspaperQuizListView.as_view(), name='news-quizs'),
    path('newsquiz/<int:pk>', views.NewspaperQuizDetailView.as_view(),
         name='news-quiz-detail')
]
