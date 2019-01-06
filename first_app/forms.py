from django import forms
from django.core import validators

class Register(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    varify_password = forms.CharField(label='Enter your passvord again:')

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        vpassword = all_clean_data['varify_password']

        if password != vpassword:
            raise forms.ValidationError("Make sure password match!")