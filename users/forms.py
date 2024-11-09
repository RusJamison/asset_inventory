from equipment.models import HealthFacility
from django import forms

class CustomSignUpForm(forms.Form):
    health_facility = forms.ModelChoiceField(
        queryset=HealthFacility.objects.all(),
        required=True,
        label="Health Facility"
    )

    def signup(self, request,user):
        pass
