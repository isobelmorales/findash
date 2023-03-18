from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TYPES = (
    ('Select', 'Select...'),
    ('asset', 'Asset'),
    ('liability', 'Liability')
)

# Create your models here.

# Account
class Account(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    type = models.CharField(
        max_length=10,
        choices = TYPES,
        default=TYPES[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show_account', kwargs={'account_id': self.id })

# Budget
class Budget(models.Model):
    category = models.CharField(max_length=50)
    planned = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse('budget_index', kwargs={'budget_id': self.id })

# Transaction
class Transaction(models.Model):
    description = models.CharField(max_length=100)
    date = models.DateField()
    account = models.ManyToManyField(Account)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    category = models.ManyToManyField(Budget)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('transactions_index')
    
    class Meta:
        ordering = ['-date']