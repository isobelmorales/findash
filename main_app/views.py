from django.shortcuts import render
from django.views.generic.edit import CreateView
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

# Create Transaction
class TransactionCreate(CreateView):
    model = Transaction
    # including all fields
    fields = '__all__'
    # redirecting to index page upon successful creation
    success_url = '/transactions/'
