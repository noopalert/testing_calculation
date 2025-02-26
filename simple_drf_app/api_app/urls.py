from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('contract_client/', installment_calculation, name='contract_client'),
]


