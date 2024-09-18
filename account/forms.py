from django import forms
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'blood_type', 'availability')