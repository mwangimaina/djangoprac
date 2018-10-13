from .models import *

from django import forms


class PublisherForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state_province = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Publisher
        fields = ('name','address','city','state_province','country','website')




class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    publication_date = forms.DateField(widget=forms.DateInput(attrs=
                                                              {'class': 'form-control',
                                                               'type':'date',
                                                              'placeholder':'Date dd/mm/yyy'}))
    class Meta:
        model = Book
        fields = ('title','authors','publisher','publication_date')
# proceed to view.py




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

