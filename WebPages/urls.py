from django.urls import path
from .views import indexPageView, suppliersPageView, forcastedSalesPageView, summaryPageView, addSuppliersPageView, deleteSuppliersPageView, updateSuppliersPageView, createSuppliersPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("suppliers/", suppliersPageView, name="suppliers"), 
    path("forecastedSales/", forcastedSalesPageView, name="forecastedSales"), 
    path("summary/", summaryPageView, name="summary"), 
    path("addSuppliers/", addSuppliersPageView, name="addSuppliers"), 
    path("deleteSuppliers/", deleteSuppliersPageView, name="deleteSuppliers"), 
    path("updateSuppliers/", updateSuppliersPageView, name="updateSuppliers"), 
    path("createSuppliers/", createSuppliersPageView, name="createSuppliers"), 

] 