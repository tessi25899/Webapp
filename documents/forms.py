from django import forms
from .models import Filedocument, Commentary

class FiledocumentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Beschreibung'}))
    document = forms.FileField()
   
    class Meta:
        model = Filedocument
        fields = ('name', 'description', 'document',)

class CommentaryForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Beschreibung'}))
    
    class Meta:
        model = Commentary
        fields = ('comment',)