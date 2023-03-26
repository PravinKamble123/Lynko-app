from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    country = forms.CharField(required=True)

    class Meta:
        fields = ['name', 'email', 'address', 'zipcode', 'city', 'state', 'country']


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password',)
