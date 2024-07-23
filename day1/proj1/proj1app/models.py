from django.db import models
class Employee(models.Model):
    name = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    class Meta:
        db_table = 'employee'

class Products(models.Model):
    pname=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    
    class Meta:
        db_table = 'products'

