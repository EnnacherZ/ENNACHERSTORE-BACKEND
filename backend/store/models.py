from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Shoe(models.Model):
    productType = models.CharField(default='Shoe', max_length=20)
    category = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    newest = models.BooleanField(default=False) 
    promo = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0)
    image = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    image1 = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    image2 = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    image3 = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    image4 = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    def __str__(self):
        return "%s %s %s"%(self.category, self.ref, self.name)

class ShoeDetail(models.Model):
    productId = models.ForeignKey(Shoe,on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s %s"%(self.productId, self.size, self.quantity)

class Sandal(models.Model):
    productType = models.CharField(default='Sandal', max_length=20)
    category = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    newest = models.BooleanField(default=False) 
    promo = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0)
    image = models.ImageField(upload_to='sandals/')
    def __str__(self):
        return "%s %s %s"%(self.category, self.ref, self.name)

class SandalDetail(models.Model):
    productId = models.ForeignKey(Sandal, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s %s"%(self.productId, self.size, self.quantity)
    
class Shirt(models.Model):
    productType = models.CharField(default='Shirt', max_length=20)
    category = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    newest = models.BooleanField(default=False) 
    promo = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0)
    image = models.ImageField(upload_to='Shirts/')
    def __str__(self):
        return "%s %s %s"%(self.category, self.ref, self.name)
    
class ShirtDetail(models.Model):
    productId = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s %s"%(self.productId, self.size, self.quantity)

class  Pant(models.Model):
    productType = models.CharField(default='Pant', max_length=20)
    category = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    newest = models.BooleanField(default=False) 
    promo = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0)
    image = models.ImageField(upload_to='Shirts/')
    def __str__(self):
        return "%s %s %s"%(self.category, self.ref, self.name)
    
class PantDetail(models.Model):
    productId = models.ForeignKey(Pant, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s %s"%(self.productId, self.size, self.quantity)