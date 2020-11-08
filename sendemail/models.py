from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120, default='')
    from_email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name
