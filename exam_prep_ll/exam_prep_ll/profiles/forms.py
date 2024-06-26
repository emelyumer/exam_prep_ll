from django import forms

from exam_prep_ll.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'email', 'password')

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First Name"
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last Name"
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email"
                },
            ),
            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "Password",
                },
            )
        }