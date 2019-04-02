from django.urls import path 
#from .views import Graph

from django.contrib import admin
from django.urls import include
from django.conf.urls import url

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# Load demo plotly apps - this triggers their registration
import performance_monitor.apps # pylint: disable=unused-import


urlpatterns = [
#  path('', Graph.as_view()),
  path('', TemplateView.as_view(template_name='performance_monitor/monitor.html'), name='monitor'),
  path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
