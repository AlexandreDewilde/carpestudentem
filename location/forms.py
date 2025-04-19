from django import forms
from .models import Location, Material

class LocationForm(forms.ModelForm):
    materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Location
        fields = ['first_name', 'name', 'email', 'location_start', 'location_end', 'phone_number', 'association', 'materials']

