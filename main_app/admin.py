from django.contrib import admin

# Import your models here.
from .models import Transaction, WalletAccount, Budget

# Register your models here.
admin.site.register(Transaction)
admin.site.register(WalletAccount)
admin.site.register(Budget)