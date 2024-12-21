from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/<int:property_id>/', views.book_property, name='book_property'),
    path('booking-success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),  # To view bookings
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),  # To cancel a booking
]