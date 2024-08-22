from django.urls import path # type: ignore
from app_myproject import views

urlpatterns = [
    path('', views.home, name="Home"),
]