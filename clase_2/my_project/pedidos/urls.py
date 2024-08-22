from django.urls import path 
from pedidos import views

urlpatterns = [
    path('pedidos', views.pedidos, name="pedidos"),
]