from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Login(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CreateHouse(forms.Form):
    Name = forms.CharField(max_length=50)


class CreateBudget(forms.Form):
    Name = forms.CharField(max_length=50)
    Target = forms.FloatField()
    Actual = forms.FloatField()


class CreateBudgetItem(forms.Form):
    Name = forms.CharField(max_length=50)
    Description = forms.CharField(max_length=150)
    Target = forms.FloatField()
    Actual = forms.FloatField()








