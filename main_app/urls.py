from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    # transactions index
    path('transactions/', views.transactions_index, name='transactions_index'),
    # add transaction
    path('transactions/add_transaction/', views.add_transaction, name='add_transaction'),
    # accounts index
    path('accounts/', views.accounts_index, name='accounts_index'),
    # show account
    path('accounts/<int:account_id>/', views.show_account, name='show_account'),
    # budgets index
    path('budgets/', views.budgets_index, name='budgets_index'),
]