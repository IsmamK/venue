from django.db import models

class Venue(models.Model):
    venue_name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(decimal_places=2,max_digits=6)
    image = models.ImageField(upload_to='venue_images/', blank=True, null=True)  # New field for image

    def __str__(self):
        return self.venue_name

class Booking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)  # Link to the Venue model
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    status=models.CharField(choices = [("pending","pending"),("approved","approved"),("rejected","rejected")],max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_number = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.venue.venue_name} on {self.date} by {self.customer_name}"


