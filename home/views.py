from django.shortcuts import render
from property.models import Property

def home(request):
    # Fetch all properties
    properties = Property.objects.all()

    # Categories for filtering
    categories = ["Beach", "Mountain", "Cabin", "Apartment"]
    selected_category = request.GET.get("category", None)
    sort_by = request.GET.get("sort_by", None)  # Get sorting parameter

    # Filter by category if selected
    if selected_category:
        properties = properties.filter(category__iexact=selected_category)

    # Sorting logic
    if sort_by == "price_low_to_high":
        properties = properties.order_by("price")
    elif sort_by == "price_high_to_low":
        properties = properties.order_by("-price")

    return render(request, "home/index.html", {
        "properties": properties,
        "categories": categories,
        "selected_category": selected_category,
        "sort_by": sort_by,
    })
