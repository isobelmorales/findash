from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    # signup
    path('accounts/signup/', views.signup, name='signup'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # wallet
    # wallet - create
    # wallet - details
    # wallet - update
    # wallet - delete
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