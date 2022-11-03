from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Crumbl Home Page')  
def suppliersPageView(request) :
    return HttpResponse('Suppliers Page') 
def forcastedSalesPageView(request) :
    return HttpResponse('Forecasted Sales Page') 
def summaryPageView(request) :
    return HttpResponse('Summary Page') 
def addSuppliersPageView(request) :
    return HttpResponse('Add Suppliers Page') 
def deleteSuppliersPageView(request) :
    return HttpResponse('Delete Suppliers Page') 
def updateSuppliersPageView(request) :
    return HttpResponse('Update Suppliers Page') 
def createSuppliersPageView(request) :
    return HttpResponse('Create Suppliers Page') 