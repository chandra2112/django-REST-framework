from django.db import models

# Create your models here.
#  this is company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    locations = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField( max_length=100,choices=(('IT','IT'),
                                                     ('Non IT','Non IT'),
                                                     ('Mobile Phone','Mobile Phone')))
    
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
    

# this is employee model

class Employee(models.Model):
    name = models.CharField (max_length=50)
    email = models.CharField(max_length=50)
    address= models.CharField( max_length=200)
    phone = models.CharField(max_length=12)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(
        ('manager','manager'),
        ('software developer','sd'),
        ('project leader','pl')

    ))
    
    company=models.ForeignKey("Company", on_delete=models.CASCADE)