from django.urls import path
from .views import indexPageView, suppliersPageView, forcastedSalesPageView, summaryPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("suppliers/", suppliersPageView, name="suppliers"), 
    path("forcastedSales/", forcastedSalesPageView, name="forcastedSales"), 
    path("summary/", summaryPageView, name="summary"), 
] 