from django.shortcuts import render
from home.models import About


# Create your views here.
def index(request):
    """A view to return the index page"""

    return render(request, 'index.html')


def about(request):
    """A view to return the about page"""

    abouts = About.objects.all()
    return render(request, 'about.html', {"abouts": abouts })

