from django.contrib import admin
from .models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'fullname',
        'email',
        'phone',
        'course_name',
        'course_date',
        'course_time',
        'order_message',
    )

    ordering = ('fullname',)


admin.site.register(Order, OrderAdmin)
