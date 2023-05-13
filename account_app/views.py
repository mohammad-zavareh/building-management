from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Otp, User
from .forms import (
    RegisterForm,
    BuildingManagerForm,
    BuildingResidentForm,
    UnitForm,
    LoginForm,
    OtpForm,
)

from building_app.models import Unit, Building

from random import randint
from datetime import datetime
from django.utils import timezone

def send_sms(code, message):
    code = str(code)
    print(message + "\n" + code)


def login_page(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            otp_code = randint(1000, 9999)

            otp_obj = Otp.objects.filter(phone_number=phone_number)

            if not otp_obj.exists():
                otp = Otp(phone_number=phone_number, code=otp_code,created=datetime.now())
                otp.save()

            else:
                otp = otp_obj.first()
                otp.code = otp_code
                otp.created = datetime.now()
                otp.save()

                print(otp.created)

            send_sms(otp_code, message='اینم از کد شما')

            request.session['phone_number'] = phone_number  # set session
            request.session.set_expiry(600)  # session expire in 10 minutes

            return redirect("account_app:login_page_otp")

    context = {
        'form': form
    }
    return render(request, 'login_page.html', context)


def login_page_otp(request):
    if 'phone_number' not in request.session:
        return redirect('account_app:login_page')

    context = {}

    phone_number = request.session['phone_number']
    otp = Otp.objects.filter(phone_number=phone_number).first()

    form = OtpForm()

    if request.method == "POST":
        form = OtpForm(request.POST)
        if form.is_valid():
            if otp.get_expire_time() == 0:
                return redirect('account_app:login_page')

            otp_entered = form.cleaned_data['otp']

            if otp_entered == otp.code:
                user = User.objects.filter(phone_number=phone_number)
                if user.exists():
                    login(request, user.first())  # first because user is list

                    unit = Unit.objects.filter(resident__phone_number=phone_number).first()
                    if unit.is_manager:
                        return redirect('building_app_manager:home')
                    else:
                        return redirect('building_app_resident:home')
                else:
                    return redirect("account_app:choice_user_type")
            else:
                context["message"] = 'کد وارد شده اشتباه است'

    context.update({
        'phone_number': phone_number,
        'expire_time': otp.get_expire_time(),
        'form': form
    })
    return render(request, 'login_page_otp.html', context)


def choice_user_type(request):
    if 'phone_number' not in request.session:
        return redirect('account_app:login_page')

    return render(request, 'choice_user_type.html')


def manager_register_page(request):
    if 'phone_number' not in request.session:
        return redirect('account_app:login_page')
    phone_number = request.session['phone_number']

    if request.method == "POST":
        register_form = RegisterForm(request.POST, prefix='register_form')
        building_form = BuildingManagerForm(request.POST, request.FILES, prefix='building_form')
        unit_form = UnitForm(request.POST, prefix='unit_form')

        if register_form.is_valid() and building_form.is_valid() and unit_form.is_valid():
            user = register_form.save(commit=False)
            user.phone_number = phone_number
            user.save()

            building = building_form.save()

            unit = unit_form.save(commit=False)
            unit.is_manager = True
            unit.building = building
            unit.resident = user
            unit.save()

            login(request, user)
            return redirect('building_app_manager:home')
    else:
        context = {
            'register_form': RegisterForm(prefix='register_form'),
            'building_form': BuildingManagerForm(prefix='building_form'),
            'unit_form': UnitForm(prefix='unit_form'),

        }
        return render(request, 'manager_register_page.html', context)


def resident_register_page(request):
    if 'phone_number' not in request.session:
        return redirect('account_app:login_page')
    phone_number = request.session['phone_number']

    if request.method == "POST":
        register_form = RegisterForm(request.POST, prefix='register_form')
        building_form = BuildingResidentForm(request.POST, prefix='building_form')
        unit_form = UnitForm(request.POST, prefix='unit_form')

        if register_form.is_valid() and building_form.is_valid() and unit_form.is_valid():
            user = register_form.save(commit=False)
            user.phone_number = phone_number
            user.save()

            building_id = building_form.cleaned_data['building_id']
            building = Building.objects.filter(building_id= building_id).first()

            unit = unit_form.save(commit=False)
            unit.building = building
            unit.resident = user
            unit.save()

            login(request, user)
            return redirect('building_app_resident:home')
    else:
        context = {
            'register_form': RegisterForm(prefix='register_form'),
            'building_form': BuildingResidentForm(prefix='building_form'),
            'unit_form': UnitForm(prefix='unit_form'),

        }
        return render(request, 'resident_register_page.html', context)

@login_required(login_url='login_page')
def logout_view(request):
    logout(request)
    return render(request, 'logout_page.html', {})