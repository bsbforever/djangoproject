from django import forms 
from models import path   
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget 
# Create your views here.

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))

class ContactForm(forms.Form):
    birth_year = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
class addpath(ModelForm):
    class Meta:
        model=path
        fields=['pathname','path']

class getpath(forms.Form):
    ipaddress=forms.IPAddressField()
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)

