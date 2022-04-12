from django.contrib import admin
from django.urls import path

from src.accounts.views import HomeView

app_name = 'accounts'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
