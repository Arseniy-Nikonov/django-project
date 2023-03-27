from django.urls import path
from marstracker.views import PlayerCreateView,PlayerUpdateView,PlayerDeleteView,PlayerList
from marstracker.views import GameList,GameCreateView,GameDeleteView,GameUpdateView,GameDetailView
from marstracker.views import GameResultCreateView,GameResultsDeleteView
from . import views
app_name = "marstracker"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('game/',GameList.as_view(),name='game-list'),
    path('game/add/',GameCreateView.as_view(),name='game-add'),
    path('game/<int:pk>',GameDetailView.as_view(),name='game-detail'),
    path('game/<int:game>/<int:player>/update',GameUpdateView.as_view(),name='game-update'),
    path('game/<int:pk>/delete/',GameDeleteView.as_view(),name='game-delete'),

    path('gameresult/<int:pk>/delete',GameResultsDeleteView.as_view(),name='game-result-delete'),
    path('gameresult/add',GameResultCreateView.as_view(),name='game-result-add'),

    path('player/',PlayerList.as_view(),name='player-list'),
    path('player/add/',PlayerCreateView.as_view(),name='player-add'),
    path('player/<int:pk>/',PlayerUpdateView.as_view(),name='player-update'),
    path('player/<int:pk>/delete/',PlayerDeleteView.as_view(),name='player-delete'),


]
