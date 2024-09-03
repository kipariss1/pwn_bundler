from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from token_bundler import endpoint_server
from token_bundler.models import WalletModel
from token_bundler.serializers import WalletSerializer

# Create your views here.

class Wallets(generics.ListCreateAPIView):
    queryset = WalletModel.objects.all()
    serializer_class = WalletSerializer


class WalletCreate(generics.CreateAPIView):
    queryset = WalletModel.objects.all()
    serializer_class = WalletSerializer


class WalletDetail(generics.RetrieveAPIView):
    queryset = WalletModel.objects.all()
    serializer_class = WalletSerializer


def _get_balance(wid, type: str):
    wallet = WalletModel.objects.get(id=wid)
    return Response(endpoint_server.wrap_balance_request(wallet=wallet.address, asset=type))

@api_view(['GET'])
def get_wallet_ballance(request, wid):
    return _get_balance(wid, 'eth')

@api_view(['GET'])
def get_wallet_erc20_assets(request, wid):
    return _get_balance(wid, 'erc20')

@api_view(['GET'])
def get_wallet_nft_assets(request, wid):
    return _get_balance(wid, 'nfts')

@api_view(['GET'])
def get_wallet_nft_collections_assets(request, wid):
    return _get_balance(wid, 'nfts_col')