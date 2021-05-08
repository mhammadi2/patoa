from django import forms
from django.core.validators import MaxValueValidator, MinLengthValidator
from .models import Patent
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# A112 = (
#     ('A112', 'Yes  '),
# )
# obj= [
#     ('obj', 'Yes  '),
# ]
# spec= [
#     ('spec', 'Yes  '),
# ]
# drw= [
#     ('drw', 'Yes  '),
# ]
# A102103= [
#     ('A102103', 'Yes  '),
# ]

class PatentForm(forms.Form):
   #patnof=forms.IntegerField()
    # A112 = forms.CharField(label= "112 Rejection", required=False, widget=forms.RadioSelect(choices=A112))
    A112 = forms.BooleanField(label= "112 Rejection",required=False)
    # A112 = forms.ChoiceField(label= "112 Rejection", required=False, choices=A112, widget=forms.RadioSelect)
    # obj = forms.CharField(label= "Objection",required=False, widget=forms.RadioSelect(choices=obj))
    obj = forms.BooleanField(label= "Objection",required=False)
    # spec = forms.CharField(label= "Spec Objection",required=False, widget=forms.RadioSelect(choices=spec))
    spec = forms.BooleanField(label= "Specfication",required=False)
    # drw = forms.CharField(label= "Draw Objection",required=False, widget=forms.RadioSelect(choices=drw))
    drw = forms.BooleanField(label= "Drawing",required=False)
    A102103 = forms.BooleanField(label= "102 & 103 Rejection",required=False)
    # A102103 = forms.CharField(label= "102/103 Rejection",required=False, widget=forms.RadioSelect(choices=A102103))


class PatForm(forms.ModelForm):
    class Meta:
        model = Patent
        #fields = ['patnof', 'claim_list']
        fields = ['patnof']
        labels = {
            'patnof': "Pat Application or PGpub Number:",
        }
