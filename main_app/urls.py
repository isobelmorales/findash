from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    # transactions index
    path('transactions/', views.transactions_index, name='transactions_index'),
    # add transaction
    path('transactions/add_transaction/', views.add_transaction, name='add_transaction'),
]