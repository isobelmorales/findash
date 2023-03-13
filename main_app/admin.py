from django.contrib import admin

# Import your models here.
from .models import Transaction

# Register your models here.
admin.site.register(Transaction)
