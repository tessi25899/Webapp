from django import forms
from .models import Event, Kindtable, Unit
import datetime


class EventForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Termin'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Termin'}))
    kind = forms.ModelChoiceField(queryset=Kindtable.objects.all().order_by('name'),widget=forms.Select(attrs={'class':'form-control','placeholder':'Termin'}),label="Welche Art",)
    unit = forms.ModelChoiceField(queryset=Unit.objects.all().order_by('name'),widget=forms.Select(attrs={'class':'form-control','placeholder':'Termin'}),label="Weclhe Einheit?")
    date = forms.DateField(initial=datetime.date.today,widget=forms.SelectDateWidget(attrs={'class':'form-control','placeholder':'Termin'}),)
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'class':' timepicker form-control','placeholder':'Termin'}))

    class Meta:
        model= Event
        fields= ('name', 'description', 'kind', 'unit', 'date', 'time')


