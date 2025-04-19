from django import forms
from .models import Couverture, CouvertureType

class CouvertureForm(forms.ModelForm):
    class Meta:
        model = Couverture
        fields = [
            'first_name', 'name', 'email', 'organizer',
            'event_name', 'place_name', 'date', 'duration_comments',
            'couverture_type', 'phone_number', 'specific_comments'
        ]
    couverture_type = forms.ModelChoiceField(
        queryset=CouvertureType.objects.all(),
        label="Type de couverture"
    )
