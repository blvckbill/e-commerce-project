from django.contrib.auth.forms import UserCreationForm
from django import forms
from store.models import Customer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        try:
            customer = Customer.objects.create(user=user)
        except Exception as e:
            # Handle customer creation error (e.g., log the error, display a user-friendly message)
            raise ValidationError('An error occurred during registration. Please try again later.')
        return user

    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('This username is already taken')

    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class LogoutForm(forms.Form):
    pass