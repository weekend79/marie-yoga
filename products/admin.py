from django.contrib import admin
from .models import AshVin, Senior, Menn


# Register your models here.
class AshVinAdmin(admin.ModelAdmin):
    list_display = (
        'ash_vin_header',
    )

    ordering = ('ash_vin_header',)


admin.site.register(AshVin, AshVinAdmin)


class SeniorAdmin(admin.ModelAdmin):
    list_display = (
        'senior_header',
    )

    ordering = ('senior_header',)


admin.site.register(Senior, SeniorAdmin)


class MennAdmin(admin.ModelAdmin):
    list_display = (
        'menn_header',
    )

    ordering = ('menn_header',)


admin.site.register(Menn, MennAdmin)
