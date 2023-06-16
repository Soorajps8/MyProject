from django.db import models

# Create your models here.
class categorydb (models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="cat_img",null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)

class productdb(models.Model):
    Category=models.CharField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="Pimg",null=True,blank=True)

