from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index, name="index"),
    path("dashboard",views.dashboard, name="dashboard"),
    path("venue-management", views.venue_management, name="venue_management"),
    path("add-venue", views.add_venue, name="add_venue"),
    path("edit-venue/<int:venue_id>/", views.edit_venue, name="edit_venue"),
    path("delete-venue/<int:venue_id>/", views.delete_venue, name="delete_venue"),
]