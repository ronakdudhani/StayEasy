from django.urls import path
from . import views

app_name = "property"

urlpatterns = [
    path('<int:pk>/', views.property_detail, name='detail'),
    path('add/step1/', views.add_property_step1, name='add_property_step1'),
    path('add/step2/', views.add_property_step2, name='add_property_step2'),
path('list/', views.property_listing, name='property_listing'),

]