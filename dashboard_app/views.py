from django.views.generic import TemplateView


class ManagerDashboard(TemplateView):
    template_name = 'manager_dashboard.html'

class ResidentDashboard(TemplateView):
    template_name = 'resident_dashboard.html'
