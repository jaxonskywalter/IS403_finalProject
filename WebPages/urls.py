from django.urls import path
from .views import indexPageView, addSuppliersPageView, deleteSuppliersPageView, updateSuppliersPageView, displaySuppliersPageView, displaySuppliersDetailPageView
from WebPages import views

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("addSuppliers/", addSuppliersPageView, name="addSuppliers"), 
    path("deleteSuppliers/", deleteSuppliersPageView, name="deleteSuppliers"), 
    path("updateSuppliers/", updateSuppliersPageView, name="updateSuppliers"), 
    path("displaySuppliers/", displaySuppliersPageView, name="displaySuppliers"),
    path("displaySuppliersDetail/", displaySuppliersDetailPageView, name="displaySuppliersDetail")
] 