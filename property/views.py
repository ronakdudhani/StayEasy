from django.shortcuts import render, get_object_or_404
from .models import Property
from django.shortcuts import render, redirect
from .forms import AddPropertyForm, AddDescriptionForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import math
import requests
from .models import Property
from geopy.distance import geodesic


def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, "property/detail.html", {"property": property})

# @login_required
# def add_property(request):
#     if request.method == "POST":
#         form = AddPropertyForm(request.POST, request.FILES)
#         if form.is_valid():
#             property_instance = form.save(commit=False)
#             property_instance.user = request.user  # Assuming a `user` field in your Property model
#             property_instance.save()
#             return redirect('property:add_details', pk=property_instance.pk)
#     else:
#         form = AddPropertyForm()

#     return render(request, 'property/add_property.html', {'form': form})

def search_address(request):
    query = request.GET.get('q', '')
    if query:
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={query}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)


def add_property_step1(request):
    if request.method == 'POST':
        print(True)
        form = AddPropertyForm(request.POST)
        print(True)
        if form.is_valid():
            print(False)
            # Store step 1 data in session
            cleaned_data = form.cleaned_data
            cleaned_data['price'] = str(cleaned_data['price'])  # Convert Decimal to string
            

            request.session['step1_data'] = form.cleaned_data
            print('i am here')
            return redirect('property:add_property_step2')
        else:
           print(form.errors)
            
    else:
        print(2)
        form = AddPropertyForm()
    return render(request, 'property/add_property.html', {'form': form})

def add_property_step2(request):
    if request.method == 'POST':
        form = AddDescriptionForm(request.POST)
        if form.is_valid():
            # Retrieve data from session and save to model
            step1_data = request.session.get('step1_data')
            if step1_data:
                property_instance = Property(**step1_data)
                property_instance.user = request.user
                property_instance.description = form.cleaned_data['description']
                property_instance.category = form.cleaned_data['category']
                property_instance.amenities = form.cleaned_data['amenities']
                property_instance.rules = form.cleaned_data['rules']
                property_instance.save()
                del request.session['step1_data']  # Clear session data after saving
                return redirect('property:add_property_step1')
    else:
        form = AddDescriptionForm()

    return render(request, 'property/add_property_description.html', {'form': form})




def property_listing(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    selected_category = request.GET.get('category', '').lower()
    sort_by = request.GET.get('sort_by', '')

    properties = Property.objects.all()

    if selected_category:
        properties = properties.filter(category__iexact=selected_category)

    if sort_by == "price_low_to_high":
        properties = properties.order_by('price')
    elif sort_by == "price_high_to_low":
        properties = properties.order_by('-price')

    property_data = []

    if lat and lon:
        user_location = (float(lat), float(lon))
        
        for property in properties:
            property_location = (property.latitude, property.longitude)
            distance = geodesic(user_location, property_location).km  # Calculate distance in kilometers
            print(distance)
            # Only include properties within 20 km
            if distance <= 20:
                property_data.append({
                    'property': property,
                    'distance': round(distance, 2)  # Round to 2 decimal places
                })
        print(property_data)
    else:
        property_data = []  # No properties if coordinates are missing

    return render(request, 'property/property_listing.html', {
        'properties': property_data,
        'search_location': f"({lat}, {lon})" if lat and lon else "Unknown Location",
        'categories': Property.objects.values_list('category', flat=True).distinct(),
        'selected_category': selected_category,
        'sort_by': sort_by,
        'lat' : lat,
        'lon' : lon,
    })
