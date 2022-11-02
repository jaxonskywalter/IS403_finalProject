from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Crumbl Home Page')  
def suppliersPageView(request) :
    return HttpResponse('Suppliers Page') 