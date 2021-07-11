from django.urls import path
from . import views
from .views import *

urlpatterns = [
   path('', views.home, name='Home'),
   path('weatherford/test_stand', views.weatherford_test_stand, name="TestStand"),
   path('weatherford/performance_test', views.weatherford_performance_test, name="PerformanceTest"),
   path('tool_changer', views.tool_changer, name="ToolChanger"),
   path('present', views.present, name="Presentation"),
   path('db', views.db, name="DB"),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),
#path('', views., name=""),




]