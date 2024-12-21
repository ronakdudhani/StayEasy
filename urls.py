from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include the users URLs
    path('', include('home.urls')),
    path('property/', include('property.urls', namespace='property')),  # Include the property app's URLs with namespace
    path('bookings/', include('bookings.urls')),

    # path('properties/', include('property.urls')),
    # path('users/', include('users.urls')),
    # path('bookings/', include('bookings.urls')),
]
