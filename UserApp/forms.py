from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, NumberInput, Select, FileInput
from .models import UserProfile



class SingUpForm(UserCreationForm):
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'pa=laceholder':'Write your username.'}))
    email=forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder':'Write your Email.'}))
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'pa=laceholder':'Write your First_name.'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'pa=laceholder':'Write your last_name.'}))

    class Meta:
        model=User
        fields=["username","email","first_name","first_name","password1","password2"]
        widgets={
            "password1":forms.PasswordInput(attrs={'placeholder':'enter your password here', "class":"form-control"}),
            "password2":forms.PasswordInput(attrs={'placeholder':'enter your password again', "class":"form-control"}),
        }


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Cairo', 'Cairo'),
    ('Alixandria', 'Alixandria'),
    ('Ismailia', 'Ismailia'),
    ('Portsied', 'Portsied'),
    ('Damita', 'Damita'),
    ('Suez', 'Suez'),
    ('Alaqsour', 'Alaqsour'),
    ('KaferElshikh', 'KaferElshikh'),
    ('Fayoun', 'Fayoun'),
    ('Sohag', 'Sohag'),
    ('Aswan', 'Aswan'),
    ('Asiot', 'Asiot'),
    ('Qena', 'Qena'),
    ('Behera', 'Behera'),
   ('ٌRedSea', 'ٌRedSea'),
   ('Monofiah', 'Monofiah'),
   ('Menea', 'Menea'),
   ('Matrooh', 'Matrooh'),
   ('Wady Gadid', 'Wady Gadid'),
   ('Qaleubiah', 'Qaleubiah'),
   ('Gharbiah', 'Gharbiah'),
   ('shamal Sinaa', 'shamal Sinaa'),
   ('Sharquiah', 'Sharquiah'),
   ('Daqahliah', 'Daqahliah'),
   ('Giza', 'Giza'),
   ('Janoob Sinaa', 'Janoob Sina'),
   ('Banysweef', 'Banysweef'),

]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }