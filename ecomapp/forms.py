from django import forms
from ecomapp.models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Name & Sure name'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Write your email'}),
            'subject': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Wrte your Subjects'}),
            'message': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write your messages'}),
        }


class SearchForm(forms.Form):
    query=forms.CharField(max_length=200)
    cat_id = forms.IntegerField()