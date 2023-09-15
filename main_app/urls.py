from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cruises/', views.cruises_index, name='cruises'),
    path('destinations/', views.destinations_index, name='destinations')

]
