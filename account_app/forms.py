from django import forms
from django.forms import ModelForm

from .models import User
from building_app.models import Building, Unit


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class BuildingManagerForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'image']


class BuildingResidentForm(forms.Form):
        building_id = forms.CharField(max_length=10)


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'number_of_member']


class LoginForm(forms.Form):
    phone_number = forms.IntegerField(label='شماره همراه')


class OtpForm(forms.Form):
    otp = forms.IntegerField(label='کد پیامک شده')