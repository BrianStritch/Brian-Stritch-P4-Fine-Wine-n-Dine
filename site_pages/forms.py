"""
    imports  -------------site_pages forms.py----------------------
"""
# third party imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserAccountDetailsForm(UserCreationForm):
    """
    Class based form to create new user with additional fields for
    first name and last name inheriting from the built in django
    usercreation form
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create user model form
        """
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            )

    def update(self, commit=True):
        """
        Class to update the users details and save to the database
        """
        user = super(UserAccountDetails, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    """
        Class based form inheriting from the built in django built
        in userchangeform the Create Review model form for
        creating a new review
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the user change form
        """
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            )
