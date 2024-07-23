from django.db import models
class Employee(models.Model):
    name = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    class Meta:
        db_table = 'Employee'

