from django.urls import path

from . import views
app_name = "marstracker"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/',views.detail,name = 'detail'),
    path('<int:game_id>/gamestatistics/', views.gamestatistics, name='gamestatistics'),
    path('addgame',views.addgame,name = 'addgame')
]
