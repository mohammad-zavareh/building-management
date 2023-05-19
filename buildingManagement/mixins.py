from django.http import Http404
from django.shortcuts import redirect

from building_app.models import Unit,ServiceCharge,Notification

def convert_to_list(list_of_dictionary):
    result = []
    for dictionaries in list_of_dictionary:
        for pk in dictionaries.values():
            result.append(str(pk))
    return result


class ManagerRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        unit = request.user.unit
        if not unit.is_manager:
            raise Http404('شما به این صفحه دسترسی ندارید')
        return super().dispatch(request, *args, **kwargs)



class ManagerAccessOwnerUnitMixin():
    def dispatch(self, request, *args, **kwargs):
        building = request.user.unit.building
        pk_units = Unit.objects.filter(building=building).values('pk')  # returned a list of dictionaries
        pk_list = convert_to_list(pk_units)

        if kwargs['pk'] in pk_list:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('شما به این صفحه دسترسی ندارید!')


class ManagerAccessOwnerChargeMixin():
    def dispatch(self, request, *args, **kwargs):
        building = request.user.unit.building
        pk_charge = ServiceCharge.objects.filter(building=building).values('pk')  # returned a list of dictionaries
        pk_list = convert_to_list(pk_charge)

        if kwargs['pk'] in pk_list:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('شما به این صفحه دسترسی ندارید!')


class ManagerAccessOwnerNotificationMixin():
    def dispatch(self, request, *args, **kwargs):
        building = request.user.unit.building
        pk_notification = Notification.objects.filter(building=building).values('pk')  # returned a list of dictionaries
        pk_list = convert_to_list(pk_notification)

        if kwargs['pk'] in pk_list:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('شما به این صفحه دسترسی ندارید!')