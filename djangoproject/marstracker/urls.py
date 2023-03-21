from django.urls import path
from marstracker.views import PlayerCreateView,PlayerUpdateView,PlayerDeleteView,PlayerList
from . import views
app_name = "marstracker"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name = 'detail'),
    path('addgame',views.addgame,name = 'addgame'),
    path('<int:game_id>/addplayer',views.addplayer,name='addplayer'),
    path('player/',PlayerList.as_view(),name='player-list'),
    path('player/add/',PlayerCreateView.as_view(),name='player-add'),
    path('player/<int:pk>/',PlayerUpdateView.as_view(),name='player-update'),
    path('player/<int:pk>/delete/',PlayerDeleteView.as_view(),name='player-delete'),

]
