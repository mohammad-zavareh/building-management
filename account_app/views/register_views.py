from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password

from datetime import datetime
from random import randint

from account_app.models import Otp, User
from account_app.forms.register_forms import (
    RegisterAccountForm,
    OtpForm,
    RegisterBuildingForm,
    RegisterUnitForm,
    DetectManagerForm
)
from building_app.models import Building


def send_sms(code, message):
    code = str(code)
    print(message + "\n" + code)


def set_otp_code(otp_code, phone_number):
    otp_obj = Otp.objects.filter(phone_number=phone_number)

    if not otp_obj.exists():
        otp = Otp(phone_number=phone_number, code=otp_code, created=datetime.now())
        otp.save()

    else:
        otp = otp_obj.first()
        otp.code = otp_code
        otp.created = datetime.now()
        otp.save()


def register_account(request):
    form = RegisterAccountForm()
    if request.method == 'POST':
        form = RegisterAccountForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']

            request.session['phone_number'] = phone_number
            request.session['is_manager'] = form.cleaned_data['is_manager']
            request.session['password'] = form.cleaned_data['password']
            request.session['first_name'] = form.cleaned_data['first_name']
            request.session['last_name'] = form.cleaned_data['last_name']

            otp_code = randint(1000, 9999)
            set_otp_code(otp_code, phone_number)
            send_sms(otp_code, message='اینم از کد شما')

            return redirect('account_app_register:verify_otp')
    context = {'form': form}
    return render(request, 'register/register-account.html', context)


def verify_otp(request):
    phone_number = request.session['phone_number']

    is_manager = request.session['is_manager']
    otp = Otp.objects.filter(phone_number=phone_number).first()
    form = OtpForm()

    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp_entered = form.cleaned_data.get('otp')
            otp_code = otp.code

            if otp.get_time_left() == 0:
                form.add_error('otp','اعتبار کد به پایان رسیده است')

            if otp_code == otp_entered:
                user = User.objects.create(
                    phone_number=phone_number,
                    is_manager=is_manager,
                    password=make_password(request.session['password']),
                    first_name=request.session['first_name'],
                    last_name=request.session['last_name'],
                )
                login(request, user)
                if is_manager:
                    return redirect('account_app_register:register_building')
                else:
                    return redirect('account_app_register:register_unit')
            else:
                form.add_error('otp','کد وارد شده اشتباه است')

    context = {
        'phone_number': phone_number,
        'expire_time': otp.get_time_left(),
        'form': form
    }
    return render(request, 'register/verify_otp.html', context)


def register_building(request):
    form = RegisterBuildingForm()
    if request.method == 'POST':
        form = RegisterBuildingForm(request.POST, request.FILES)
        if form.is_valid():
            building = form.save(commit=False)
            building.manager = request.user
            building.save()

            return redirect('dashboard_app:manager_dashboard')

    context = {'form': form}
    return render(request, 'register/register-building.html', context)


def register_unit(request):
    unit_form = RegisterUnitForm(prefix='unit_form')
    detect_form = DetectManagerForm(prefix='manager_form')
    if request.method == 'POST':
        unit_form = RegisterUnitForm(request.POST, prefix='unit_form')
        detect_form = DetectManagerForm(request.POST, prefix='manager_form')

        if unit_form.is_valid() and detect_form.is_valid():
            # detect manager
            phone_number_of_manager = detect_form.cleaned_data.get('phone_number_of_manager')
            building = Building.objects.filter(manager__phone_number=phone_number_of_manager).first()

            unit = unit_form.save(commit=False)
            unit.resident = request.user
            unit.building = building
            unit.save()
            return redirect('dashboard_app:resident_dashboard')

    context = {
        'unit_form': unit_form,
        'manager_form': detect_form
    }
    return render(request, 'register/register-unit.html', context)
