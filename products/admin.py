from django.contrib import admin
from .models import AshVin


# Register your models here.
class AshVinAdmin(admin.ModelAdmin):
    list_display = (
        'ash_vin_header',
    )

    ordering = ('ash_vin_header',)


admin.site.register(AshVin, AshVinAdmin)
