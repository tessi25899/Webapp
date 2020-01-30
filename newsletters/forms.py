from django import forms
from .models import Topic, News
from profiles.models import Profile
import datetime


class NewsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Titel'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Nachricht'}))
    topic = forms.ModelChoiceField(queryset=Topic.objects.all().order_by('name'),widget=forms.Select(attrs={'class':'form-control','placeholder':'Thema'}))
    published = forms.DateField(initial=datetime.date.today,widget=forms.SelectDateWidget(attrs={'class':'form-control','placeholder':'Datum'}))
    created_by = forms.ModelChoiceField(queryset=Profile.objects.all(),widget=forms.Select(attrs={'class':'form-control','placeholder':'Ersteller'}))

    class Meta:
        model = News
        fields = ('name', 'message', 'topic', 'published', 'created_by')


class TopicForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Thema'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Beschreibung'}))

    class Meta:
        model = Topic
        fields = ('name','description',)