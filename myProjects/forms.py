from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, MyProjects,Rating
import datetime as dt


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_image', 'bio']

class MyProjectsForm(forms.ModelForm):
    class Meta:
        model = MyProjects
        fields = ('image', 'title', 'projecturl', 'description')

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']        

