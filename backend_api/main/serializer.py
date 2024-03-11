from rest_framework import serializers
from . import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Vendor
        fields=['id', 'user', 'address']
        
    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Vendor
        fields=['id', 'user', 'address']
        
    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
                
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Product
        fields=['id', 'category','vendor', 'Name','Description', 'higher_price','unit_price', 'Stock']

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
        
        
class SpeciesListSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Species
        fields=['Species_ID', 'species_Name',]
    def __init__(self, *args, **kwargs):
        super(SpeciesListSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1    
        
class SpeciesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Species
        fields=['Species_ID', 'species_Name',]
    def __init__(self, *args, **kwargs):
        super(SpeciesDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1           
        
class RacesSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Vendor
        fields=['id', 'Name',]
        
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Vendor
        fields=['id', 'Name',]
        
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Product
        fields=['id', 'Inventory_ID',]




class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Product
        fields=['id', 'name','surname', 'email','address', 'telephone_number']


        

class OrdesrSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Product
        fields=['id', 'date','customer_id', 'product_id','quantity' ]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Product
        fields=['id', 'detail_id','order_id', 'product_id','quantity','unit_price' ]
