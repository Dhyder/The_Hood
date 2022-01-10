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


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')
    


class NeighbourHoodForm(forms.ModelForm):
    hood_logo = ImageField(label='')
    
    class Meta:
        model = NeighbourHood
        fields = ('hood_logo','name','location','admin','description','health_tell','police_number',)
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')
