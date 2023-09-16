from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookings/', views.bookings_index, name='index'),
    path('bookings/<int:booking_id>/', views.bookings_detail, name='detail'),
    path('bookings/create/', views.BookingCreate.as_view(), name='bookings_create'),
    path('bookings/<int:pk>/update/', views.BookingUpdate.as_view(), name='bookings_update'),
    path('bookings/<int:pk>/delete/', views.BookingDelete.as_view(), name='bookings_delete'),
    path('bookings/<int:booking_id>/add_room/', views.add_room, name='add_room'),
    path('bookings/<int:booking_id>/assoc_cruise/<int:cruise_id>/', views.assoc_cruise, name='assoc_cruise'),
    path('bookings/<int:booking_id>/unassoc_cruise/<int:cruise_id>/', views.unassoc_cruise, name='unassoc_cruise'),
    path('bookings/<int:booking_id>/assoc_user/<int:user_id>/', views.assoc_user, name='assoc_user'),
    path('bookings/<int:booking_id>/unassoc_user/<int:user_id>/', views.unassoc_user, name='unassoc_user'),
    path('cruises/', views.cruises_index, name='cruises'),
    path('cruises/<int:cruise_id>/', views.cruise_detail, name='cruise_detail'),
    path('cruises/<int:cruise_id>/assoc_destination/<int:destination_id>/', views.assoc_destination, name='assoc_destination'),
    path('destinations/', views.destinations_index, name='destinations'),
    path('destinations/<int:destination_id>/', views.destinations_detail, name='destinations_detail'),
]   
