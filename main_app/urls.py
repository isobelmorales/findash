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
    # transactions - update
    # transactions - delete
    # budget
    path('budget/', views.budget_index, name='budget_index'),
    # budget - create
    # budget - update
    # budget - delete
    # add association
    # add unassociation
]