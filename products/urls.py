from django.urls import path
from . import views


urlpatterns = [
    path('ash_vin', views.ash_vin, name="ash_vin"),
    path('senior', views.senior, name="senior"),
    path('menn', views.menn, name="menn"),
]
