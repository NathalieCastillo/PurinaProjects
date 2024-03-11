from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#modificable
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username


#category
class ProductCategory(models.Model):
    title= models.CharField(max_length=200)
    detail= models.TextField(null=True)

    def __str__(self):
        return self.title
    
    
#produt table    
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    Name= models.CharField(max_length=200)
    Description= models.TextField(null=True)
    higher_price= models.FloatField()
    unit_price= models.FloatField()
    Stock= models.CharField(max_length=200)

    def __str__(self):
        return self.Name
    
class SpeciesCategory(models.Model):
    Id_Species= models.CharField(max_length=200)
    name= models.TextField(null=False)

    def __str__(self):
        return self.name
    


class Species(models.Model):
    tipe = models.ForeignKey(SpeciesCategory, on_delete=models.SET_NULL, null=False, related_name='Species_category')


    def __str__(self):
        return self.tipe


class Races(models.Model):
    Race_ID = models.TextField(null=True)
    race_name = models.TextField(null=True)
    
    
    def __str__(self):
        return self.race_name
    
    
class Food(models.Model):
    Food_ID = models.TextField(null=True)
    name = models.TextField(null=True)
    Type = models.TextField(null=True)
    
    
    def __str__(self):
        return self.name


#aqui debe de ir inventario


class Inventory(models.Model):
    Inventory_ID = models.TextField(null=True)

    
    
    def __str__(self):
        return self.Inventory_ID
    

class Client(models.Model):
    client_id = models.TextField(null=True)
    name = models.TextField(null=True)
    surname = models.TextField(null=True)
    email = models.TextField(null=True)
    address = models.TextField(null=True)
    telephone_number = models.TextField(null=True)

    
    
    def __str__(self):
        return self.name
    
    
class Orders(models.Model):
    order_id = models.TextField(null=True)
    date = models.TextField(null=True)
    customer_id = models.TextField(null=True)
    product_id = models.TextField(null=True)
    quantity = models.TextField(null=True)

    
    
    def __str__(self):
        return self.date
    

class ProductDetail(models.Model):
    detail_id= models.CharField(max_length=200)
    order_id= models.TextField(null=True)
    product_id= models.CharField(max_length=200)
    quantity= models.CharField(max_length=200)
    unit_price= models.TextField(null=True)

    def __str__(self):
        return self.detail_id