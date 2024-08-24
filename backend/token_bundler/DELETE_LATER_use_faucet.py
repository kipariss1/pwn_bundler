from web3 import Web3
from backend.token_bundler.endpoint import ENDPOINT

w3 = Web3(Web3.HTTPProvider(ENDPOINT))

abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"}],"name":"drip","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"t1155","outputs":[{"internalType":"contract PWNFaucet1155","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"t20D","outputs":[{"internalType":"contract PWNFaucet20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"t20S","outputs":[{"internalType":"contract PWNFaucet20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"t721","outputs":[{"internalType":"contract PWNFaucet721","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'
contract_address = '0x3A04ea90bAb53fBDB9C07B0D08ED865244114c91'

contract_instance = w3.eth.contract(address=contract_address, abi=abi)

nonce = w3.eth.get_transaction_count('0x3A04ea90bAb53fBDB9C07B0D08ED865244114c91')
chain_id = w3.eth.chain_id
private_key = 'MY_PRIVATE_KEY'
caller = '0xaE08A0a2F7C8e1Dc94a6C350240e6574fF5B1BA0'
call_function = contract_instance.functions.drip(caller).build_transaction({"chainId": chain_id, "from": caller, "nonce": nonce})
signed_tx = w3.eth.account.sign_transaction(call_function, private_key=private_key)
send_tx = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)