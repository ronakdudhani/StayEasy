from django.db import models



class Property(models.Model):
    # Existing fields
    user = models.TextField(max_length=20,null=True)
    name = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=50)
    availability_start = models.DateField(blank=True, null=True)
    availability_end = models.DateField(blank=True, null=True)
    image_url = models.URLField(max_length=1000)  # Updated field for image URL

    # New fields
    amenities = models.TextField(blank=True, null=True)  # List of amenities (comma-separated or JSON)
    rules = models.TextField(blank=True, null=True)      # List of rules for the property

    def __str__(self):
        return self.name
