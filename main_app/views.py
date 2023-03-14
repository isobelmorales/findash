from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Transaction, Account, Budget
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

# Accounts Index
def accounts_index(request):
    accounts = Account.objects.all()

    return render(request, 'accounts/index.html', { 'accounts': accounts })

# Show Account
def show_account(request, account_id):
    account = Account.objects.get(id=account_id)

    return render(request, 'accounts/show.html', { 'account': account })

# Create Account
class AccountCreate(CreateView):
    model = Account
    fields = '__all__'

# Update Account
class AccountUpdate(UpdateView):
    model = Account
    fields = ['balance', 'type']

# Delete Account
class AccountDelete(DeleteView):
    model = Account
    success_url = '/accounts/'

# Budget Index
def budgets_index(request):
    budgets = Budget.objects.all()

    return render(request, 'budgets/index.html', { 'budgets': budgets })