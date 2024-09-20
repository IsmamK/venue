from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    # client side
    path("",views.index, name="index"), # home page
    path("book/<int:venue_id>/", views.book_venue, name="book_venue"),  #booking page
    path("booking-success/<int:booking_id>/", views.booking_success, name="booking_success"),  # booking success page
 
    # admin side

    #dashboard
    path("dashboard",views.dashboard, name="dashboard"),

     #venue management
    path("venue-management", views.venue_management, name="venue_management"),
    path("add-venue", views.add_venue, name="add_venue"),
    path("edit-venue/<int:venue_id>/", views.edit_venue, name="edit_venue"),
    path("delete-venue/<int:venue_id>/", views.delete_venue, name="delete_venue"),

    #booking management
    path("booking-management", views.booking_management, name="booking_management"),
    path('update_booking/<int:booking_id>/', views.update_booking, name='update_booking'),
    path("delete-booking/<int:booking_id>/", views.delete_booking, name="delete_booking"),
]