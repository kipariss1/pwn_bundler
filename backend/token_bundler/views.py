from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from rest_framework import generics
from rest_framework.response import Response

from token_bundler import endpoint_server
from token_bundler.models import WalletModel
from token_bundler.serializers import WalletSerializer

# Create your views here.

class Wallets(generics.ListCreateAPIView):
    queryset = WalletModel.objects.all()
    serializer_class = WalletSerializer

class WalletDetail:
    # TODO: finish wallet details with generics
    pass

@require_http_methods(['GET'])
def get_wallet_ballance(request, wid):
    wallet = WalletModel.objects.filter(id=wid)
    return Response(endpoint_server.get_wallet_balance(wallet=wallet.address))

@require_http_methods(['GET'])
def get_wallet_erc20_assets(request, wid):
    wallet = WalletModel.objects.filter(id=wid)
    return None

@require_http_methods(['GET'])
def get_wallet_nft_assets(request, wid):
    wallet = WalletModel.objects.filter(id=wid)
    return None
