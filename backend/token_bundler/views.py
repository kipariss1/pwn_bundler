from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from token_bundler import endpoint_server
from token_bundler.models import WalletModel
from token_bundler.serializers import WalletSerializer 

# Create your views here.

class Wallet(APIView):

    def get(self, request):
        wallet = request.data['wallet']
        return Response(endpoint_server.get_wallet_balance(wallet=wallet))

    def post(self, request):
        # create wallet
        address = request.POST['address']
        name = request.POST['name'] if 'name' in request.POST.keys() else ''
        new_wallet = WalletModel(
            address=address,
            name=name
        )
        new_wallet.save()
        serializer = WalletSerializer(new_wallet)
        return Response(serializer.data)
