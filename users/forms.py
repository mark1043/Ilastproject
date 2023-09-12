from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ModelForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
             'username',
             'email',
             'password1',
             'password2'
        ]

class CustomUserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)