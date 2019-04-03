from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # チュートリアルの元コードは→url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('<slug:room_name>/', views.room, name='room'),
]

