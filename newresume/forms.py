from django import forms
from newresume.models import Users,SignIn,LogIn
from newresume.models import SignIn

class UserForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'


class SigninForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=SignIn
        fields='__all__'


class LoginForm(forms.ModelForm):
    user_password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=LogIn
        fields='__all__'
