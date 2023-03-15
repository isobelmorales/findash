from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    # signup
    path('accounts/signup/', views.signup, name='signup'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # accounts
    path('wallet/accounts/', views.accounts_index, name='accounts_index'),
    # accounts - create
    path('wallet/accounts/create/', views.AccountCreate.as_view(), name='accounts_create'),
    # accounts - show
    path('wallet/accounts/<int:account_id>/', views.show_account, name='show_account'),
    # accounts - update
    path('wallet/accounts/<int:pk>/update/', views.AccountUpdate.as_view(), name='accounts_update'),
    # accounts - delete
    path('wallet/accounts/<int:pk>/delete/', views.AccountDelete.as_view(), name='accounts_delete'),
    # transactions
    path('transactions/', views.transactions_index, name='transactions_index'),
    # transactions - create
    path('transactions/create/', views.create_transaction, name='create_transaction'),
    # add association
    path('transactions/<int:transaction_id>/assoc_account/<int:account_id>/', views.assoc_account, name='assoc_account'),
    path('transactions/<int:transaction_id>/assoc_budget/<int:budget_id>/', views.assoc_budget, name='assoc_budget'),
    # add unassociation
    path('transactions/<int:transaction_id>/unassoc_account/<int:account_id>/', views.unassoc_account, name='unassoc_account'),
    path('transactions/<int:transaction_id>/unassoc_budget/<int:budget_id>/', views.unassoc_budget, name='unassoc_budget'),
    # transactions - update
    # transactions - delete
    # budget
    path('budget/', views.budget_index, name='budget_index'),
    # budget - create
    path('budget/create/', views.create_budget, name='create_budget'),
    # budget - update
    # budget - delete
    # add association
    # add unassociation
]