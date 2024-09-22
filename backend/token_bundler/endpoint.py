from typing import Optional
from web3 import Web3
from moralis import evm_api
from typing import Literal
from django.conf import settings

ENDPOINT_ADDRESS = settings.ENDPOINT_ADDRESS
MORALIS_API_KEY = settings.MORALIS_API_KEY
NET_TYPE = settings.NET_TYPE

assetType = Literal['eth', 'erc20', 'nfts', 'nfts_col']

class EndpointServer:

    def __init__(
            self, 
            endpoint_address: Optional[str] = None,
            moralis_api_key: Optional[str] = None,
        ) -> None:
        self.endpoint_address = endpoint_address if endpoint_address else ENDPOINT_ADDRESS
        self.w3 = Web3(Web3.HTTPProvider(self.endpoint_address))
        if not self.w3.is_connected():
            raise ConnectionError("Couldn't establish connection to endpoint address")
        self.moralis_api_key = moralis_api_key if moralis_api_key else MORALIS_API_KEY

    def wallet_exists(self, wallet: str) -> bool:
        return self.w3.is_address(wallet)
        
    def get_wallet_balance(self, wallet: str):
        balance_in_wei = self.w3.eth.get_balance(wallet)
        return self.w3.from_wei(balance_in_wei, 'ether')
    
    def get_wallet_erc20_assets(self, wallet: str):
        params = {
            "address": wallet,
            "chain": NET_TYPE,
        }
        return evm_api.token.get_wallet_token_balances(
            api_key=self.moralis_api_key,
            params=params
        )
    
    def get_wallet_nft_assets(self, wallet: str):
        params = {
            "chain": NET_TYPE,
            "format": "decimal",
            "media_items": False,
            "address": wallet
        }
        return evm_api.nft.get_wallet_nfts(
            api_key=self.moralis_api_key, 
            params=params
        )


    def get_wallet_nft_collections_assets(self, wallet: str):
        params = {
            "address": wallet,
            "chain": NET_TYPE,
            "limit": 100,
            "cursor": "",
        }
        return evm_api.nft.get_wallet_nft_collections(
            api_key=self.moralis_api_key,
            params=params,
        )
    
    def wrap_balance_request(self, wallet: str, asset: assetType = 'eth'):
        if asset == 'eth':
            return self.get_wallet_balance(wallet=wallet)
        elif asset == 'erc20':
            return self.get_wallet_erc20_assets(wallet=wallet)
        elif asset == 'nfts':
            return self.get_wallet_nft_assets(wallet=wallet)
        elif asset == 'nfts_col':
            return self.get_wallet_nft_collections_assets(wallet=wallet)
