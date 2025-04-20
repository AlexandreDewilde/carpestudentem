from django.urls import path
from .views import latest_team_view

urlpatterns = [
    path('', latest_team_view, name='team'),
]
