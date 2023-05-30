from django.urls import path
from .views import home, about, customer

urlpatterns = [
    path("", home),
    path("about/", about),
    path("customer/", customer),
]
