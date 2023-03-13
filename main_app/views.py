from django.shortcuts import render
from .models import Transaction

# Create your views here.

# Home
def home(request):
    return render(request, 'home.html')

# Transactions Index
def transactions_index(request):
    # collecting transaction model/info from SQL
    transactions = Transaction.objects.all()
    return render(request, 'transactions/index.html', { 'transactions': transactions })