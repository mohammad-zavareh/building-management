from django.contrib import admin

from .models import RequestPayment


class RequestPaymentAdmin(admin.ModelAdmin):
    list_display = ('building', 'sheba_number',
                    'amount',
                    'paid',
                    'pay_time',
                    'request_time'
                    )

    list_filter = ('building','amount')
    ordering = ('request_time',)
    search_fields = ('sheba_number','building')


admin.site.register(RequestPayment, RequestPaymentAdmin)