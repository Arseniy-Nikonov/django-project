from django.urls import path

from . import views
app_name = "marstracker"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name = 'detail'),
    path('addgame',views.addgame,name = 'addgame'),
    path('<int:game_id>/addplayer',views.addplayer,name='addplayer')

]
