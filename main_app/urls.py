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
    # accounts - details
    # accounts - update
    # accounts - delete
    # transactions
    # transactions - create
    # transactions - update
    # transactions - delete
    # budget
    # budget - create
    # budget - update
    # budget - delete
    # add association
    # add unassociation
]