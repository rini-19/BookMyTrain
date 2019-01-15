from django import forms
from django.core import validators
from first_app.models import Register
from django.contrib.admin import widgets
from django.forms import ModelForm

from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
)

User = get_user_model()

GENDER = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    varify_password = forms.CharField(label='Confirm Password:', widget=forms.PasswordInput)
    dob = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    class Meta:
        model= Register
        fields= '__all__'

    def clean(self, *args, **kwargs):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        varify_password = cleaned_data.get("confirm_password")

        if varify_password != password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )
        return super(RegisterForm, self).clean(*args, **kwargs)

class userLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def cleaned(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user= authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('This user does not exists!')
            if not user.check_password(password):
                raise forms.ValidationError('password is incorrect!')
            if not user.is_active:
                raise forms.ValidationError('This user is no longer active.')
            return super(userLoginForm, self).clean(*args, **kwargs)
