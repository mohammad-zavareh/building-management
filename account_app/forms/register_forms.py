from django import forms
from django.forms import ModelForm

from account_app.models import User
from building_app.models import Building, Unit


class RegisterAccountForm(ModelForm):


    class Meta:
        model = User
        fields = ['is_manager', 'phone_number', 'password', 'first_name', 'last_name']
        widgets = {
            'phone_number': forms.NumberInput(attrs={'placeholder': 'تلفن همراه'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}),
            'is_manager': forms.CheckboxInput(),
            'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور'})
        }




class OtpForm(forms.Form):
    otp = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'کد پیامک شده'}),
        label='کد پیامک شده'
    )


class RegisterBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'image', 'rules']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام ساختمان'}),
            'rules': forms.Textarea(attrs={'placeholder': 'قوانین ساختمان'}),
        }
        labels = {
            'name': 'نام ساختمان',
            'image': 'تصویر ساختمان',
            'rules': 'قوامین ساختمان'
        }


class RegisterUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'number_of_member']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام واحد'}),
            'number_of_member': forms.NumberInput(attrs={'placeholder': 'تعداد اعضای ساختمان'}),
        }


class DetectManagerForm(forms.Form):
    phone_number_of_manager = forms.IntegerField(
        label='شماره همراه مدیر ساختمان',
        widget=forms.NumberInput(attrs={'placeholder': 'شماره مدیر ساختمان'})
    )
