from django.db import models

# Create your models here.
class User(models.Model):
    ROLES = (('customer', 'Customer'),('partner', 'Partner'), ('tailor', 'Tailor'),('office', 'Office') )

    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='customer'
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.TextField()
    def __str__(self):
        return self.id

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_logo = models.ImageField(upload_to ='uploads/category')
    category_sale = models.IntegerField()
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_logo = models.ImageField(upload_to ='uploads/product')
    product_price = models.IntegerField()
    product_short = models.CharField(max_length=100)
    product_long = models.TextField()
    product_sale = models.IntegerField()
    def __str__(self):
        return self.product_name

class Product_images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/product_images')
    
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart_user = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_quantity = models.IntegerField()
    def __str__(self):
        return self.cart_product