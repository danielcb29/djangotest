__author__ = 'daniel'
import forms
from  prueba.models import *
#from django import newforms as forms

class InvestigadorForm(forms.ModelForm):
    class Meta:
        model = Investigador


