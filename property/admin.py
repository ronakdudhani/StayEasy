from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'category', 'price')
