from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'guests', 'checkin_date', 'checkout_date']

    

class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, label="Card Number")
    expiry_date = forms.CharField(max_length=5, label="Expiry Date (MM/YY)")
    cvv = forms.CharField(max_length=3, label="CVV")
