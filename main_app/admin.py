from django.contrib import admin

# Import your models here.
from .models import Transaction, Account, Budget

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Account)
admin.site.register(Budget)