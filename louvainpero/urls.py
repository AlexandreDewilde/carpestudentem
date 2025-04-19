from django.urls import path
from . import views

urlpatterns = [
    path("", views.louvainpero_view, name="louvainpero"),
]
