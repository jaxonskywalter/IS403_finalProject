from django.urls import path
from .views import indexPageView, addSuppliersPageView, deleteSuppliersPageView, updateSuppliersPageView, displaySuppliersPageView, displaySuppliersDetailPageView, getSuppliersDetailPageView, updateSinglePageView
from WebPages import views

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("addSuppliers/", addSuppliersPageView, name="addSuppliers"), 
    path("deleteSuppliers/<int:id>/", deleteSuppliersPageView, name="deleteSuppliers"), 
    path("/displaySuppliers/<int:id>/", updateSinglePageView, name="updateSingle"),
    path("updateSuppliers/", updateSuppliersPageView, name="updateSuppliers"),  
    path("displaySuppliers/", displaySuppliersPageView, name="displaySuppliers"),
    path("getSuppliersDetail/<int:id>/", getSuppliersDetailPageView, name="getSuppliersDetail"),
    path("displaySuppliersDetail/", displaySuppliersDetailPageView, name="displaySuppliersDetail")
] 