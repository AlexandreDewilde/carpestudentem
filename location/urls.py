from django.urls import path
from .views import location_view

urlpatterns = [
    path('', location_view, name='location'),
    path("success", location_view, name="location_success"),
]
