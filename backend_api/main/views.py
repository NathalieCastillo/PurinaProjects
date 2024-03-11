from rest_framework import generics, permissions
from . import serializer
from . import models
# Create your views here.

class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializer.VendorSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializer.VendorDetailSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductListSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductDetailSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
class SpeciesList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Species.objects.all()
    serializer_class = serializer.SpeciesListSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Species.objects.all()
    serializer_class = serializer.SpeciesDetailSerializer
    #permission_classes = [permissions.IsAuthenticated]