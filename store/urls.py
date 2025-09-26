from django.urls import path
from .views import dashboard, create_customer

urlpatterns = [
    path('', dashboard),
    path('create/', create_customer)
]