from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, NeighbourHood, Business, Post
from pyuploadcare.dj.forms import ImageField


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text=None)
    error_messages = {
    'password_mismatch': ("The two password fields didn't match."),
}
    password1 = forms.CharField(
    label=("Password"),
    strip=False,
    widget=forms.PasswordInput,
)
    password2 = forms.CharField(
    label=("Password confirmation"),
    widget=forms.PasswordInput,
    strip=False,
)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
