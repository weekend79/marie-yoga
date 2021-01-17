from django.shortcuts import render
from products.models import AshVin


# Create your views here.
def ashvin(request):
    """A view to return the Ashtanga - Vinyasa course"""

    ashvins = AshVin.objects.all()
    return render(request, 'ashtanga-vinyasa.html', {"ashvins": ashvins})


def senior(request):
    """A view to return the Senior courses"""

    return render(request, 'senior.html')


def menn(request):
    """A view to return the men courses"""

    return render(request, 'menn.html')
