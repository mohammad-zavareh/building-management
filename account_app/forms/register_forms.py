from django import forms
from django.forms import ModelForm

from account_app.models import User
from building_app.models import Building, Unit


class RegisterAccountForm(ModelForm):
    re_password = forms.CharField(max_length=100,
                                  label='تکرار رمز عبور',
                                  widget=forms.PasswordInput(attrs={'placeholder': ' تکرار رمز عبور'})
                                  )

    class Meta:
        model = User
        fields = ['is_manager', 'phone_number', 'password', 're_password', 'first_name', 'last_name']
        widgets = {
            'phone_number': forms.NumberInput(attrs={'placeholder': 'تلفن همراه'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}),
            'is_manager': forms.CheckboxInput(),
            'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور'})
        }

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password:
            return re_password
        raise forms.ValidationError('رمز عبور با تکرار رمز عبور تطابق ندارد!')


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

    def clean_phone_number_of_manager(self):
        phone_number_of_manager = self.cleaned_data.get('phone_number_of_manager')
        building = Building.objects.filter(manager__phone_number=phone_number_of_manager)
        if not building.exists():
            raise forms.ValidationError('مدیری با این شماره موبایل وجود ندارد!')
        return phone_number_of_manager