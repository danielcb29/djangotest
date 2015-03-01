__author__ = 'daniel'
import forms
from  prueba.models import *

class InvestigadorForm(forms.ModelForm):
    class Meta:
        model = Investigador