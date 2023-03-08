from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:player_id>/',views.detail,name = 'detail'),
    path('<int:player_id>/results/', views.results, name='results'),
    path('<int:player_id>/vote/', views.vote, name='vote'),
]
