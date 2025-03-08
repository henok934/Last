# forms.py
from django import forms

class UsernameEmailForm(forms.Form):
    username = forms.CharField(required=False, max_length=150)
    email = forms.EmailField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if not username and not email:
            raise forms.ValidationError("You must provide either your username or your email.")
        return cleaned_data

