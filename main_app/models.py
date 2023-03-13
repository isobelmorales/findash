from django.db import models

# Create your models here.

# Transaction
class Transaction(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    account = models.CharField(max_length=50)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name