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
