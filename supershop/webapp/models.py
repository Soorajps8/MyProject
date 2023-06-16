from django.db import models

# Create your models here.
class Registerdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="pro_img",null=True,blank=True)
