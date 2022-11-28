from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Article


class UserForm(ModelForm):
    """
    Form for user creation
    """
    class Meta:
        model = User
        fields = ['username', 'password']
