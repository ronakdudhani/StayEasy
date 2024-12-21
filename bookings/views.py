from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, PaymentForm
from .models import Booking
from django.contrib.auth.decorators import login_required
from property.models import Property
import time
from datetime import datetime


@login_required
def book_property(request, property_id):
    # Fetch the property using the property_id
    property = Property.objects.get(id=property_id)

    # Extract the parameters from the URL or request
    checkin_date = request.GET.get('checkin_date')
    checkout_date = request.GET.get('checkout_date')
    guests = request.GET.get('guests')
    print("===============")
    print(checkin_date, checkout_date)
    print(guests)

    # Set the initial values for the booking form fields
    initial_data = {
        'checkin_date': checkin_date,
        'checkout_date': checkout_date,
        'guests': guests
    }

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        payment_form = PaymentForm(request.POST)

        print(booking_form.is_valid())
        print(payment_form.is_valid())

        print(booking_form.errors)

        if booking_form.is_valid() and payment_form.is_valid():
            # Save booking details
            checkin_date = booking_form.cleaned_data['checkin_date']
            checkout_date = booking_form.cleaned_data['checkout_date']
            # Calculate the number of days stayed
            num_days = (checkout_date - checkin_date).days

            if num_days <= 0:
                booking_form.add_error('checkout_date', "Check-out date must be after check-in date.")
                return render(request, 'bookings/book_property.html', {
                    'property': property,
                    'booking_form': booking_form,
                    'payment_form': payment_form,
                })

            # Calculate the total price
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.property = property
            booking.total_price = property.price * booking.guests * num_days
            booking.save()

            # Process the payment (mocked here)
            payment_details = payment_form.cleaned_data
            print(f"Payment processed for {booking.user.username}: {payment_details}")

            return redirect('bookings:booking_success', booking_id=booking.id)
    else:
        booking_form = BookingForm(initial=initial_data)
        payment_form = PaymentForm()

    return render(request, 'bookings/book_property.html', {
        'property': property,
        'booking_form': booking_form,
        'payment_form': payment_form,
    })


@login_required
def booking_success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'bookings/booking_success.html', {'booking': booking})



@login_required
def my_bookings(request):
    # Retrieve all bookings of the logged-in user
    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'bookings/my_bookings.html', {
        'bookings': bookings,
    })

@login_required
def cancel_booking(request, booking_id):
    # Get the booking instance by ID
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    # Cancel the booking (you can either delete it or mark it as cancelled)
    booking.delete()  # Or if you want to mark it as cancelled: booking.status = 'Cancelled'

    # Redirect to the bookings page after cancellation
    return redirect('bookings:my_bookings')

