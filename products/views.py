from django.shortcuts import render


# Create your views here.
def ash_vin(request):
    """A view to return the Ashtanga - Vinyasa course"""

    return render(request, 'ashtanga-vinyasa.html')


def senior(request):
    """A view to return the Senior courses"""

    return render(request, 'senior.html')


def menn(request):
    """A view to return the men courses"""

    return render(request, 'menn.html')
