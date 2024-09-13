from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def index(request):
    venues = Venue.objects.all()
    return render(request,"index.html",{
        "venues":venues
    })

    
def dashboard(request):
    return render(request, "dashboard.html")

def venue_management(request):
    venues = Venue.objects.all()
    return render(request, "venue_management.html", {"venues": venues})

def add_venue(request):
    if request.method == "POST":
        venue_name = request.POST['venue_name']
        capacity = request.POST['capacity']
        location = request.POST['location']
        hourly_rate = request.POST['hourly_rate']
        image = request.FILES.get('image')

     
        Venue.objects.create(venue_name=venue_name, capacity=capacity, location=location, hourly_rate=hourly_rate, image=image)

        return redirect('venue_management')
    else:
        return render(request, "add_venue.html")

def edit_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    
    if request.method == "POST":
        venue.venue_name = request.POST['venue_name']
        venue.capacity = request.POST['capacity']
        venue.location = request.POST['location']
        venue.hourly_rate = request.POST['hourly_rate']
        
        if 'image' in request.FILES:
            venue.image = request.FILES['image']

        venue.save()
        return redirect('venue_management')
    else:
       return render(request, "edit_venue.html", {"venue": venue})

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('venue_management')