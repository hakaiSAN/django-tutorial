from django.urls import path
from . import views 

urlpatterns = [
  path('', views.view_over, name='view_over'),
  path('view1', views.view1, name='view1'),
  path('view2', views.view2, name='view2'),
]
