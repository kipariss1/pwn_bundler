from django.urls import path
from token_bundler import views as views

urlpatterns = [
    path('wallet/', view=views.Wallet.as_view(), name='wallet')
]


