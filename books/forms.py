__author__ = 'daniel'
from django import forms
from django.forms import ModelForm
from books.models import *
TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)

class BookForm(ModelForm):
    class Meta:
        model = Book;
        fields = ['title','authors','publisher','publication_date']


