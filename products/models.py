from django.db import models


# Create your models here.
class AshVin(models.Model):
    ash_vin_header = models.CharField(max_length=120, default='')
    header_text = models.TextField(max_length=1024, null=True, blank=True)
    ash_vin_content = models.TextField(null=True, blank=True)
    ash_vin_content_2 = models.TextField(null=True, blank=True)
    ash_vin_content_3 = models.TextField(null=True, blank=True)
    ash_vin_content_4 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.ash_vin_header


class Senior(models.Model):
    senior_header = models.CharField(max_length=120, default='')
    senior_text = models.TextField(max_length=1024, null=True, blank=True)
    senior_content = models.TextField(null=True, blank=True)
    senior_content_2 = models.TextField(null=True, blank=True)
    senior_content_3 = models.TextField(null=True, blank=True)
    senior_content_4 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.senior_header


class Menn(models.Model):
    menn_header = models.CharField(max_length=120, default='')
    menn_text = models.TextField(max_length=1024, null=True, blank=True)
    menn_content = models.TextField(null=True, blank=True)
    menn_content_2 = models.TextField(null=True, blank=True)
    menn_content_3 = models.TextField(null=True, blank=True)
    menn_content_4 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.menn_header


class Live(models.Model):
    live_header = models.CharField(max_length=120, default='')
    live_content = models.TextField(null=True, blank=True)
    live_content_2 = models.TextField(null=True, blank=True)
    live_content_3 = models.TextField(null=True, blank=True)
    live_content_4 = models.TextField(null=True, blank=True)
    live_content_5 = models.TextField(null=True, blank=True)
    live_content_6 = models.TextField(null=True, blank=True)
    live_content_7 = models.TextField(null=True, blank=True)
    pris = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.live_header
