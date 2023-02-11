from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=30,required=True,help_text="your email")
    class Meta:
        model = User
        fields = ["username", "password1", "password2","email",]
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            print('hi')
            user.save()
        return user