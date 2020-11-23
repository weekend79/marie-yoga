from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import OrderForm
from order.models import Order


# Create your views here.
def orderView(request):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        if (request.method == 'POST'):
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            order_course_name = request.POST.get('course_name')
            order_course_date = request.POST.get('course_date')
            order_course_time = request.POST.get('course_time')
            order_message = request.POST.get('order_message')
            try:
                order = Order(fullname=fullname, email=email, phone=phone,
                              course_name=course_name, course_date=course_date,
                              course_time=course_time,
                              order_message=order_message)

                order.save()
            except BadHeaderError:
                return HttpResponse('Ugyldig rute')
            return redirect('success')
    return render(request, 'order.html', {'form': form})


def successView(request):
    return render(request, 'success.html')
