from django.db import models

# Create your models here.
class Applicants(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    uimage = models.TextField()

    class Meta:
        db_table = 'tbl_applicant'


    
