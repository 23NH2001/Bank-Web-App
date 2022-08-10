from pyexpat import model
from django.db import models

# Create your models here.
class Customer(models.Model):
    account_type = (
        ("S","Saving Account"),
        ("C","Checkin Account"),
        ("FD","Fixed Deposite")
    )

    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    accountNumber = models.CharField(max_length=20)
    account = models.CharField(max_length=2, choices=account_type)
    password = models.CharField(max_length=50)
    amount = models.FloatField(default=None)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.fname
        
