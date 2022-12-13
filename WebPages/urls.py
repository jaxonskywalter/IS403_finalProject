from django.urls import path
from .views import indexPageView, addSuppliersPageView, deleteSuppliersPageView, updateSuppliersPageView, displaySuppliersPageView, displaySuppliersDetailPageView, updateSinglePageView
from WebPages import views

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("addSuppliers/", addSuppliersPageView, name="addSuppliers"), 
    path("/deleteSuppliers/<int:id>/", deleteSuppliersPageView, name="deleteSuppliers"),
    path("/displaySuppliers/", displaySuppliersPageView, name="displaySuppliers"),
    path("displaySuppliersDetail/", displaySuppliersDetailPageView, name="displaySuppliersDetail"),
    path("/updateSuppliers/" , updateSuppliersPageView, name="updateSuppliers"),
    path("/displaySuppliers/<int:id>/" , updateSinglePageView, name="updateSingle"),
] 