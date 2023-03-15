# Imports
from django.forms import ModelForm
from .models import Transaction
from django import forms

class TransactionForm(ModelForm):
    template_name = 'form_snippet.html'
    class Meta:
        model = Transaction
        fields = ['description', 'date', 'account', 'amount', 'category']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'MM-DD-YYYY'}),
            'account': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }