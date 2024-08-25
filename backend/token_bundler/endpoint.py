from typing import Optional
from web3 import Web3

ENDPOINT_ADDRESS = 'https://eth-sepolia.g.alchemy.com/v2/63BGWEBc08wM_UJVo3lVsgHIrRlacnuM'


class EndpointServer:

    def __init__(self, endpoint_address: Optional[str] = None) -> None:
        self.endpoint_address = endpoint_address if endpoint_address else ENDPOINT_ADDRESS
        self.w3 = Web3(Web3.HTTPProvider(self.endpoint_address))
        if not self.w3.is_connected():
            raise ConnectionError("Couldn't establish connection to endpoint address")
        
    def get_wallet_balance(self, wallet: str):
        return self.w3.eth.get_balance(wallet)
