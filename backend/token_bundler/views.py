from django.shortcuts import render
from token_bundler.wallet import WALLET
from token_bundler import endpoint_server
from rest_framework.views import APIView

# Create your views here.

class Wallet(APIView):

    def get(self, request):
        pass

