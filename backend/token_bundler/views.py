from django.shortcuts import render
from token_bundler.wallet import WALLET
from token_bundler import endpoint_server
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Wallet(APIView):

    def get(self, request):
        wallet = request.data['wallet']
        return Response(endpoint_server.get_wallet_balance(wallet=wallet))

