from django.shortcuts import render
from courses.models import Course


# Create your views here.
def all_courses(request):
    """A view that renders all the courses listed from admin"""
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})
