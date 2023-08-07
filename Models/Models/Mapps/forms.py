from django import forms

class user_form(forms.Form):
    user_name=forms.CharField(max_length=20,required=False,
    label="Full Name",widget=forms.TextInput(
    attrs={'placeholder':"Enter your full name",'style':'width:170px'}))

    user_dob=forms.DateField(label="Date Field",
    widget=forms.TextInput(attrs={'type':'date'}))

    user_email=forms.EmailField(required=False,label="User Email")

from typing import Any, Dict
from django import forms
from django.core import validators
from Mapps import models


class Musician_Form(forms.ModelForm):
    class Meta:
        model=models.Musician
        fields=('first_name','last_name',)
        fields="__all__"


        

        
