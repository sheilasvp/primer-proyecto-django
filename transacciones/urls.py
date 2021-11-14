from django.urls import path
from transacciones import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('create-person', views.create_person),
    path('create-transaction', views.create_transaction),
    path('balance', views.get_balance)
]
