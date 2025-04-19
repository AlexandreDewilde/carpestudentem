from django.urls import path
from .views import couverture_view

urlpatterns = [
    path('', couverture_view, name='couverture'),
]
