from django.db import models
from django.urls import reverse

# Create your models here.

# Account
class Account(models.Model):
    name = models.CharField(max_length=50)
    balance = models.IntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show_account', kwargs={'account_id': self.id })

# Transaction
class Transaction(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    account = models.CharField(max_length=50)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Budget
class Budget(models.Model):
    category = models.CharField(max_length=50)
    planned = models.IntegerField()
    actual = models.IntegerField()

    def __str__(self):
        return self.name