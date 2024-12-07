from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review


class RegisterForm(UserCreationForm):
    """
    Custom form used to allow users to sign up for the application
    """
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    university = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'university')

    def clean_email(self):
        """
        Clean the email field specifically to ensure it is saved in lowercase
        """
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
        return email

    def clean(self):
        """
        Evaluates the validity of the fields within the form
        """
        cleaned_data = super().clean()

        # Validate email uniqueness
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', f"There is already an account linked to the email address '{email}'")
        return cleaned_data


class ReviewForm(forms.ModelForm):
    """
    Form for submitting internship reviews with detailed information
    """
    class Meta:
        model = Review
        fields = [
            "title",
            "company_name",
            "description",
            "overall_experience",
            "skills_required",
            "skills_learned",
            "duration",
            "compensation",
            "location",
            "rating",
            "opinion",
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the internship'}),
            'overall_experience': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your overall experience'}),
            'skills_required': forms.Textarea(attrs={'rows': 4, 'placeholder': 'What skills were required?'}),
            'skills_learned': forms.Textarea(attrs={'rows': 4, 'placeholder': 'What skills did you learn?'}),
            'opinion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your opinion about the internship'}),
        }
