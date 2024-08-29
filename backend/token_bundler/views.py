from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view

from token_bundler import endpoint_server
from token_bundler.models import WalletModel
from token_bundler.serializers import WalletSerializer

# Create your views here.

class Wallets(generics.ListCreateAPIView):
    queryset = WalletModel.objects.all()
    serializer_class = WalletSerializer


class WalletDetail(mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = WalletModel.objects.all()
    serializer_class = WalletSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)
    
    def post(self, request, pk, *args, **kwargs):
        return self.create(request, pk, args, kwargs)


@api_view(['GET'])
def get_wallet_ballance(request, wid):
    wallet = WalletModel.objects.get(id=wid)
    return Response(endpoint_server.get_wallet_balance(wallet=wallet.address))

@api_view(['GET'])
def get_wallet_erc20_assets(request, wid):
    wallet = WalletModel.objects.filter(id=wid)
    return None

@api_view(['GET'])
def get_wallet_nft_assets(request, wid):
    wallet = WalletModel.objects.filter(id=wid)
    return None
