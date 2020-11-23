from django.db import models


# Create your models here.
class Order(models.Model):
    fullname = models.CharField(max_length=125, default='')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    course_name = models.CharField(max_length=125)
    course_date = models.DateField(max_length=20)
    course_time = models.TimeField(max_length=20)
    order_message = models.TextField()

    def __str__(self):
        return self.fullname
