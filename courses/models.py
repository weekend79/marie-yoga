from django.db import models


# Create your models here.
class Course(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    duration = models.CharField(max_length=254,
                                null=True, blank=True)
    coursedate = models.DateField(null=True, blank=True)
    coursetime = models.TimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    fullname = models.CharField(max_length=125, default='')
    email = models.EmailField(max_length=254, null=False,
                              blank=False)
    phone = models.CharField(max_length=20)
    course_name = models.CharField(max_length=125)
    course_date = models.DateField()
    course_time = models.TimeField()
    order_message = models.TextField()

    def __str__(self):
        return self.course_name
