from django import forms
from .models import Property

class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'price', 'address', 'latitude', 'longitude', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class AddDescriptionForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    category = forms.ChoiceField(choices=[('apartment', 'Apartment'), ('house', 'House'),('cabin', 'Cabin'),('beach', 'Beach'),('mountain', 'Mountain')], widget=forms.Select(attrs={'class': 'form-control'}))
    amenities = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Amenities'}))
    rules = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Rules'}))
