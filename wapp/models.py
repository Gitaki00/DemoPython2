from django.db import models

# Create your models here.
class Link(models.Model):
    address=models.CharField(max_length=500,null=True,blank=True)
    string_name=models.CharField(max_length=500,null=True,blank=True)
