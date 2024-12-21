from django.utils import timezone
from django.db import models
from property.models import Property

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.TextField(max_length=20,null=True)
    guests = models.IntegerField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)



    @staticmethod
    def is_available(property, checkin_date, checkout_date):
        """Check if the property is available between the given dates."""
        overlapping_bookings = Booking.objects.filter(
            property=property,
            checkin_date__lt=checkout_date,
            checkout_date__gt=checkin_date
        )
        return not overlapping_bookings.exists()
