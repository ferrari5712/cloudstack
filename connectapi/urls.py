from . import views
from django.urls import path

urlpatterns = [
    path('urlconnect/', views.apiconnect, name='urlconnect')
]
