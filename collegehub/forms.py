from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """
    Custom form used to allow users to sign up for the application
    """
    first_name = forms.CharField(max_length=50, required=True)
    """The first name of the new user"""

    last_name = forms.CharField(max_length=50, required=True)
    """The last name of the new user"""

    email = forms.EmailField(max_length=254, required=True)
    """The email address of the new user"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def clean(self):
        """
        Evaluates the validity of the fields within the form

        :return: A mapping of all valid fields
        """
        cleaned_data = super().clean()

        # If one of the other fields was invalid, it will have already been caught, so we only need to
        # check the custom stuff here
        email = cleaned_data['email']  # type: str

        validations = list()

        # Email address is currently the best way to identify who a user really is. Hopefully that will change,
        # but we need to check to make sure that there aren't duplicate identities under different names.
        if User.objects.filter(email=email).exists():
            field = "email"
            message = "There is already an account linked to the email address '{}'".format(email)
            validations.append({"field": field, "message": message})

        # Attach all identified broken validations to the form
        for validation in validations:
            self.add_error(validation['field'], validation['message'])

        # If no validations were encountered, we can go ahead and return the cleaned data
        if len(validations) == 0:
            return cleaned_data

