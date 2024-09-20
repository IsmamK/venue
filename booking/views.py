from django.shortcuts import render, redirect
from .models import *
# Create your views here.


# ----------------- CLIENT SIDE VIEWS --------------------

def index(request):
    venues = Venue.objects.all()
    return render(request,"index.html",{
        "venues":venues
    })

def book_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)

    if request.method == "POST":
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        customer_name = request.POST['customer_name']
        customer_number = request.POST['customer_number']

        # Create the booking
        booking = Booking.objects.create(
            venue=venue,
            date=date,
            start_time=start_time,
            end_time=end_time,
            customer_name=customer_name,
            customer_number=customer_number,
            status="pending"
        )

        # Redirect to the success page with booking details
        return redirect('booking_success', booking_id=booking.id)

    return render(request, "book_venue.html", {"venue": venue})

def booking_success(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)

    return render(request, "booking_success.html", {
        "booking": booking,
        
        
        })



# ----------------- ADMIN SIDE VIEWS --------------------

def dashboard(request):
    return render(request, "dashboard.html")

# Venue Management

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

# Booking Management

def booking_management(request):
    bookings = Booking.objects.all()
    return render(request, "booking_management.html", {"bookings": bookings})

def update_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)

    if request.method == 'POST':
        status = request.POST.get('status')
        booking.status = status
        booking.save()
        return redirect('booking_management')

    # If not POST, redirect to management page
    return redirect('booking_management')

def delete_booking(request, booking_id):
    booking =Booking.objects.get(id=booking_id)
    booking.delete()
    return redirect('booking_management')