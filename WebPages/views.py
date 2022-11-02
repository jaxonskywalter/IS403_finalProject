from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Crumbl Home Page')  
def suppliersPageView(request) :
    return HttpResponse('Suppliers Page') 
def forcastedSalesPageView(request) :
    return HttpResponse('Forcasted Sales Page') 
def summaryPageView(request) :
    return HttpResponse('Summary Page') 
