from django.urls import path
from . import views


urlpatterns = [
    path('ashvin', views.ashvin, name="ashvin"),
    path('senior', views.senior, name="senior"),
    path('menn', views.menn, name="menn"),
]
