from django.urls import path
from . import views

urlpatterns = [
    #vendors
    path('vendors/', views.VendorList.as_view()),
    path('vendor/<int:pk>/', views.VendorDetail.as_view()),
    
    path('Species/', views.SpeciesList.as_view()),
    path('Specie/<int:pk>/', views.SpeciesDetail.as_view()),
]