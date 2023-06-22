from django import forms

from account_app.models import User


class LoginForm(forms.Form):
    phone_number = forms.IntegerField(
        label='شماره همراه',
        widget=forms.NumberInput(attrs={'placeholder': 'شماره همراه'})
    )


class OtpForm(forms.Form):
    otp = forms.IntegerField(
        label='کد پیامک شده',
        widget=forms.NumberInput(attrs={'placeholder': 'کد پیامک شده'})
    )


class PasswordForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'})
    )
