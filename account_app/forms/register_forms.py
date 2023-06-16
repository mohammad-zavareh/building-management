from django import forms
from django.forms import ModelForm

from account_app.models import User
from building_app.models import Building, Unit


class RegisterAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['is_manager', 'phone_number', 'password', 'first_name', 'last_name']


class OtpForm(forms.Form):
    otp = forms.IntegerField(label='کد پیامک شده')


class RegisterBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'image', 'rules']


class RegisterUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'number_of_member']


class DetectManagerForm(forms.Form):
    phone_number_of_manager = forms.IntegerField(label='شماره همراه مدیر ساختمان')
