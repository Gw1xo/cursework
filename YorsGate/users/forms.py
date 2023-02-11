from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None
