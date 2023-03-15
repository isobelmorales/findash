from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Account, Transaction, Budget
from .forms import TransactionForm, BudgetForm


# Create your views here.

# Home
def home(request):
    return render(request, 'home.html')

# Sign Up
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Accounts - Index
@login_required
def accounts_index(request):
    accounts = Account.objects.filter(user=request.user)
    return render(request, 'accounts/index.html', { 'accounts': accounts })

# Create Account
class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    fields = ['name', 'balance', 'type']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Show Account
@login_required
def show_account(request, account_id):
    account = Account.objects.get(id=account_id)

    return render(request, 'accounts/show.html', { 'account': account })

# Update Account
class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    fields = ['balance', 'type']

# Delete Account
class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = '/wallet/accounts/'

# Transactions
@login_required
def transactions_index(request):
    transactions = Transaction.objects.filter(user=request.user)

    transaction_form = TransactionForm()

    return render(request, 'transactions/index.html', { 'transactions': transactions, 'transaction_form': transaction_form })

# Create Transaction
@login_required
def create_transaction(request):
    form = TransactionForm(request.POST)

    if form.is_valid():
        instance.user = request.user
        new_transaction = form.save(commit=False)
        new_transaction.save()
        form.save_account()
        form.save_budget()
    
    return redirect('transactions_index')

# Update Transaction
# Delete Transaction

# Budget
@login_required
def budget_index(request):
    budgets = Budget.objects.filter(user=request.user)

    budget_form = BudgetForm()

    return render(request, 'budgets/index.html', { 'budgets': budgets, 'budget_form': budget_form })

# Create Budget
@login_required
def create_budget(request):
    form = BudgetForm(request.POST)

    if form.is_valid():
        form.instance.user = request.user
        new_budget = form.save(commit=False)
        new_budget.save()
    
    return redirect('budget_index')

# Update Budget
# Delete Budget