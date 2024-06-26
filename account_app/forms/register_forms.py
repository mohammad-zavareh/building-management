from django import forms
from django.forms import ModelForm

from account_app.models import User
from building_app.models import Building, Unit
from vip_service_app.models import VipService


class RegisterAccountForm(ModelForm):
    re_password = forms.CharField(max_length=100,
                                  label='تکرار رمز عبور',
                                  widget=forms.PasswordInput(
                                      attrs={'placeholder': ' تکرار رمز عبور', 'class': 'input100'})
                                  )

    class Meta:
        model = User
        fields = ['is_manager', 'phone_number', 'password', 're_password', 'first_name', 'last_name']
        widgets = {
            'phone_number': forms.NumberInput(attrs={'placeholder': 'تلفن همراه', 'class': 'input100'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'نام', 'class': 'input100'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'نام خانوادگی', 'class': 'input100'}),
            'is_manager': forms.CheckboxInput(attrs={'class': 'input100'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور', 'class': 'input100'})
        }

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password:
            return re_password
        raise forms.ValidationError('رمز عبور با تکرار رمز عبور تطابق ندارد!')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        user = User.objects.filter(phone_number=phone_number)
        if user.exists():
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است!')
        return phone_number


class OtpForm(forms.Form):
    otp = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'کد پیامک شده'}),
        label='کد پیامک شده'
    )


class RegisterBuildingForm(ModelForm):
    max_unit = forms.ChoiceField(
        choices=VipService.MAX_UNIT_CHOICE,
        widget=forms.Select(attrs={'class': 'input100'})
    )

    class Meta:
        model = Building
        fields = ['name', 'image', 'max_unit', 'rules', 'card_type', 'card_number', 'owner_card']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام ساختمان', 'class': 'input100'}),
            'rules': forms.Textarea(attrs={'placeholder': 'قوانین ساختمان', 'class': 'input100'}),
            'card_type': forms.Textarea(attrs={'placeholder': 'نوع کارت', 'class': 'input100'}),
            'card_number': forms.NumberInput(attrs={'placeholder': 'شماره کارت', 'class': 'input100'}),
            'owner_card': forms.NumberInput(attrs={'placeholder': 'صاحب کارت', 'class': 'input100'}),
        }
        labels = {
            'name': 'نام ساختمان',
            'image': 'تصویر ساختمان',
            'rules': 'قوانین ساختمان',
            'card_type': 'نوع کارت',
            'card_number': 'شماره کارت',
            'owner_card': 'صاحب کارت',
        }


class RegisterUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'number_of_member']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام واحد', 'class': 'input100'}),
            'number_of_member': forms.NumberInput(attrs={'placeholder': 'تعداد اعضای ساختمان', 'class': 'input100'}),
        }


class DetectManagerForm(forms.Form):
    phone_number_of_manager = forms.IntegerField(
        label='شماره همراه مدیر ساختمان',
        widget=forms.NumberInput(attrs={'placeholder': 'شماره مدیر ساختمان', 'class': 'input100'})
    )

    def clean_phone_number_of_manager(self):
        phone_number_of_manager = self.cleaned_data.get('phone_number_of_manager')
        building = Building.objects.filter(manager__phone_number=phone_number_of_manager)
        if not building.exists():
            raise forms.ValidationError('مدیری با این شماره موبایل وجود ندارد!')
        return phone_number_of_manager
