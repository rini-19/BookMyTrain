from django import forms
from django.core import validators
from first_app.models import Register
from django.contrib.admin import widgets
from django.forms import ModelForm

from django.contrib.auth import authenticate, get_user_model, login, logout


User = get_user_model()
#GENDER = (
#    ('F', 'Female'),
#    ('M', 'Male'),
#    ('O', 'Other'),
#)

class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    #gender = forms.CharField(max_length=1, choices=GENDER)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    vpassword = forms.CharField(label='Confirm Password:', widget=forms.PasswordInput)
    dob = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            #'gender',
            'dob',
            'username',
            'password',
            'vpassword',
        ]

    def clean_vpassword(self):
        password = self.cleaned_data.get("password")
        vpassword = self.cleaned_data.get("vpassword")

        if vpassword != password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )
        return password

class userLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        print(username)

        if username and password:
            print("check")
            user= authenticate(username = username, password = password)
            print("check auth")
            if not user:
                raise forms.ValidationError('This user does not exists!')
                print("VALIDATION error")
            if not user.check_password(password):
                raise forms.ValidationError('password is incorrect!')
                print("VALIDATION error")
            if not user.is_active:
                raise forms.ValidationError('This user is no longer active.')
        return super(userLoginForm, self).clean(*args, **kwargs)
