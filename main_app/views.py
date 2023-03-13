from django.shortcuts import render

# temporary transactions seed
transactions = [
    {'name': 'Trader Joe\'s', 'date': 'March 12, 2023', 'account': 'AmEx', 'amount': '$50', 'category': 'Groceries'},
    {'name': 'Bluestone Lane', 'date': 'March 13, 2023', 'account': 'Cash', 'amount': '$10', 'category': 'Food & Drinks'}
]

# Create your views here.

# Home
def home(request):
    return render(request, 'home.html')

# Transaction Index
def transactions_index(request):
    return render(request, 'transactions/index.html', { 'transactions': transactions })