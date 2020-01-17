from django import forms
from .models import Event, Kindtable, Unit
import datetime


class EventForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Termin'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Beschreibung'}))
    kind = forms.ModelChoiceField(queryset=Kindtable.objects.all().order_by('name'),widget=forms.Select(attrs={'class':'form-control','placeholder':'Termin'}),label="Kategorie",)
    unit = forms.ModelChoiceField(queryset=Unit.objects.all().order_by('name'),widget=forms.Select(attrs={'class':'form-control','placeholder':'Termin'}),label="Einheit")
    date = forms.DateField(initial=datetime.date.today,widget=forms.SelectDateWidget(attrs={'class':'form-control','placeholder':'Datum'}),)
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'class':' timepicker form-control','placeholder':'ss:mm'}))

    class Meta:
        model = Event
        fields = ('name', 'description', 'kind', 'unit', 'date', 'time',)


class KindForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Kategorie'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Beschreibung'}))

    class Meta:
        model = Kindtable
        fields = ('name','description',)
