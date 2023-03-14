from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Transaction
from .forms import TransactionForm

# Create your views here.

# Home
def home(request):
    return render(request, 'home.html')

# Transactions Index
def transactions_index(request):
    # collecting transaction model/info from SQL
    transactions = Transaction.objects.all()

    # instantiate TransactionForm to be rendered in the modal in the template
    transaction_form = TransactionForm()

    return render(request, 'transactions/index.html', { 'transactions': transactions, 'transaction_form': transaction_form })

# Create Transaction

def add_transaction(request):
    form = TransactionForm(request.POST)

    if form.is_valid():
        new_transaction = form.save(commit=False)
        new_transaction.save()
    
    return redirect('transactions_index')