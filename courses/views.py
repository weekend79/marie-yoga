from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import OrderForm
from datetime import datetime
from courses.models import Order, Course


# Create your views here.
def all_courses(request):
    """A view that renders all the courses listed from admin"""
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})


def orderView(request):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        if (request.method == 'POST'):
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            course_date = request.POST.get('course_date')
            course_time = request.POST.get('course_time')
            order_message = request.POST.get('order_message')
            try:
                order = Order(fullname=fullname, email=email, phone=phone,
                              subject=subject, course_date=course_date,
                              course_time=course_time,
                              order_message=order_message,
                              date=datetime.today())
                order.save()
            except BadHeaderError:
                return HttpResponse('Ugyldig rute')
            return redirect('success')
    return render(request, 'courses.html', {'order': order})
