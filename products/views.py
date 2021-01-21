from django.shortcuts import render
from products.models import AshVin, Senior, Menn


# Create your views here.
def ashvin(request):
    """A view to return the Ashtanga - Vinyasa course"""

    ashvins = AshVin.objects.all()
    return render(request, 'ashtanga-vinyasa.html', {"ashvins": ashvins})


def senior(request):
    """A view to return the Senior courses"""

    seniors = Senior.objects.all()
    return render(request, 'senior.html', {"seniors": seniors})


def menn(request):
    """A view to return the men courses"""

    menns = Menn.objects.all()
    return render(request, 'menn.html', {"menns": menns})
