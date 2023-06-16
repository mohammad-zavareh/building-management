from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from random import randint
from account_app.forms.login_forms import LoginForm, OtpForm, PasswordForm
from .register_views import send_sms, set_otp_code
from account_app.models import Otp, User

from datetime import datetime

def login_account(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            request.session["phone_number"] = phone_number

            otp_code = randint(1000, 9999)
            set_otp_code(otp_code, phone_number)
            send_sms(otp_code, message='اینم از کد شما')

            return redirect('account_app_login:verify_otp')

    context = {'form': form}
    return render(request, 'login/login-account.html', context)


def verify_password(request):
    phone_number = request.session['phone_number']

    form = PasswordForm()
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = User.objects.filter(phone_number=phone_number, password=password)

            if user.exists():
                user = user.first()
                login(request, user)
                del request.session['phone_number']

                if user.is_manager:
                    return redirect("dashboard_app:manager_dashboard")
                else:
                    return redirect("dashboard_app:resident_dashboard")
            else:
                print('کاربری با این شماره و رمز عبور وجود ندارد!')

    context = {'form': form}
    return render(request, 'login/verify-password.html', context)


def verify_otp(request):
    phone_number = request.session['phone_number']

    otp = Otp.objects.filter(phone_number=phone_number).first()

    form = OtpForm()
    if request.method == "POST":
        form = OtpForm(request.POST)
        if form.is_valid():
            otp_entered = form.cleaned_data['otp']
            otp_code = otp.code

            if otp_code == otp_entered:
                user = User.objects.filter(phone_number=phone_number)
                if user.exists():
                    user = user.first()
                    login(request, user)
                    del request.session['phone_number']
                    if user.is_manager:
                        return redirect('dashboard_app:manager_dashboard')
                    else:
                        return redirect('dashboard_app:resident_dashboard')
                print('کاربری با این شماره وجود ندارد')
            else:
                print('کد وارد شده اشتباه است')

    context = {
        'phone_number': phone_number,
        'expire_time': otp.get_time_left(),
        'form': form
    }
    return render(request, 'login/verify-otp.html', context)


@login_required(login_url='account_app_login:login_account')
def logout_view(request):
    logout(request)
    return render(request, 'login/logout_page.html', {})
