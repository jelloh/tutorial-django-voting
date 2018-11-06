from django.urls import path
from . import views

app_name = 'votings'

urlpatterns = [
    # ex: /votings/
    path('', views.index, name='index'),
    # ex: /votings/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /votings/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /votings/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]