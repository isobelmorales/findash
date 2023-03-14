# Imports
from django.forms import ModelForm
from .models import Transaction

class TransactionForm(ModelForm):
    template_name = 'form_snippet.html'
    class Meta:
        model = Transaction
        fields = '__all__'
        labels = {
            'name': 'Name',
            'date': 'Date',
            'account': 'Account',
            'amount': 'Amount',
            'category': 'Category'
        }