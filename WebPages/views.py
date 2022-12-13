from django.http import HttpResponse
from django.shortcuts import render
from WebPages.models import Supplier, Ingredient

def indexPageView(request) :
    return render(request, 'WebPages/index.html')
def addSuppliersPageView(request) :
    return render(request, 'WebPages/addSupplier.html')
def deleteSuppliersPageView(request) :
    return render(request, 'WebPages/deleteSupplier.html')
def updateSuppliersPageView(request) :
    return render(request, 'WebPages/updateSupplier.html')
def displaySuppliersPageView(request) :
    data = Supplier.objects.all()
    context = {
        'supplier' : data
    }
    return render(request, 'WebPages/displaySupplier.html', context)
def displaySuppliersDetailPageView(request):
    return render(request, 'WebPages/detailSupplier.html')
