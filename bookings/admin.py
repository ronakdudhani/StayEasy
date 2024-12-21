from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('property','user',  'guests', 'checkin_date', 'checkout_date')
    list_filter = ('checkin_date', 'checkout_date', 'property')
    search_fields = ('user__username', 'property__name')
