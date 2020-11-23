from django.db import models


# Create your models here.
class About(models.Model):
    about_header = models.CharField(max_length=120, default='')
    header_text = models.TextField(max_length=1024, null=True, blank=True)
    header_text_2 = models.TextField(max_length=1024, null=True, blank=True)
    about_content = models.TextField(null=True, blank=True)
    about_content_2 = models.TextField(null=True, blank=True)
    about_content_3 = models.TextField(null=True, blank=True)
    about_content_4 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.about_header
