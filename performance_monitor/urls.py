from django.urls import path 
from .views import Graph

urlpatterns = [
  path('', Graph.as_view()),
]
