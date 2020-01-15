from django import forms
from .models import Unit

class UnitCreateForm(forms.ModelForm):
    class Meta:
        model= Unit
        fields= ('slug', 'name', 'street', 'housenumber', 'postcode', 'place', 'day', 'starttime', 'endtime')
