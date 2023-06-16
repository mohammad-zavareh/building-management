from django import forms

from account_app.models import User


class LoginForm(forms.Form):
    phone_number = forms.IntegerField(label='شماره همراه')


class OtpForm(forms.Form):
    otp = forms.IntegerField(label='کد پیامک شده')

class PasswordForm(forms.Form):
    password = forms.CharField(label='رمز عبور')