from django.urls import path
from .views import indexPageView, suppliersPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("suppliers/", suppliersPageView, name="suppliers"), 
] 