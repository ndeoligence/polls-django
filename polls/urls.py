from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # maps /polls/
    path('', views.index, name='index'),
    # maps [eg]: /polls/3/
    path('<int:question_id>/', views.detail, name='detail'),
    # maps [eg]: /polls/3/results/
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
