from django.http import HttpResponse
from django.shortcuts import render
from WebPages.models import Supplier

# Shows the home page
def indexPageView(request) :
    return render(request, 'WebPages/index.html')

def addSuppliersPageView(request) :
    # Allows the user to add a supplier if they click the add button
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']

        # Saves all the supplier's information
        supplier = Supplier(name=name, email=email, phone=phone, location=location)
        supplier.save()
        return displaySuppliersPageView(request)
    return render(request, 'WebPages/addSupplier.html')

def deleteSuppliersPageView(request) :
    return render(request, 'WebPages/deleteSupplier.html')

def updateSuppliersPageView(request) :
    return render(request, 'WebPages/updateSupplier.html')

# Shows all the suppliers on a page
def displaySuppliersPageView(request) :
    data = Supplier.objects.all()
    context = {
        'supplier' : data,
        'results' : ''
    }

    # If the user presses the search button 
    if request.method == 'POST':
        find = request.POST.get('find')
        data = Supplier.objects.filter(name=find)
        # If the search retreives data this dynamically changes the page to show the results
        if data.count() > 0:
            context['supplier'] = data
        # If the search doesn't return any results this tells the user that there are no matches to their input
        else:
            context['results'] = 'No suppliers exist with the name you entered.'
    return render(request, 'WebPages/displaySupplier.html', context)

# Allows the user to see all the data pertaining to a specific supplier  
def getSuppliersDetailPageView(request, id):
    supplier = Supplier.objects.get(id=id)
    context = {
        'supplier' : supplier
    }
    return render(request, 'WebPages/detailSupplier.html', context)

def displaySuppliersDetailPageView(request):
    return render(request, 'WebPages/detailSupplier.html')

# Deletes a specific supplier's records
def deleteSuppliersPageView(request, id) :
    data = Supplier.objects.get(id = id)

    data.delete()

    return displaySuppliersPageView(request)    

def updateSuppliersPageView(request) :
    if request.method == 'POST':
        id = request.POST['id']

        supplier = Supplier.objects.get(id=id)

        supplier.name = request.POST['name']
        supplier.email = request.POST['email']
        supplier.phone = request.POST['phone']


        supplier.save()

    return displaySuppliersPageView(request)

# Gets a supplier's ID from the database and passes it to the updateSuppliersPageView to be updated
def updateSinglePageView(request, id):
    data = Supplier.objects.get(id = id)
    
    context = {
        'supplier' : data,
    }
    return render(request, 'WebPages/updateSupplier.html', context)
