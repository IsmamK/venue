from django.db import models

class Venue(models.Model):
    venue_name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(decimal_places=2,max_digits=6)
    image = models.ImageField(upload_to='venue_images/', blank=True, null=True)  # New field for image


class Booking(models.Model):
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    status=models.CharField(choices = [("pending","pending"),("approved","approved"),("rejected","rejected")],max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_number = models.IntegerField()

