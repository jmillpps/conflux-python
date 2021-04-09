from src.Wallet import Wallet
from src.RPC import HTTPClient
from src.Util import randomkey
import json

wallet = Wallet(private_key=randomkey(32), type='user', network_prefix='cfx')
address = wallet.public_address()
old_address = wallet.old_public_address()
print(f'Wallet Address: {address}')
print(f'Old Wallet Address: {old_address}')
message = b'Message for ECDSA signing'
print(f'Test Message: {message}')
signature = wallet.sign(message)
print(f'Signature: {signature.hex()}')
recovered_keys = Wallet.Address.recover_possible_addresses(signature, message, wallet.type, wallet.network_prefix)
print('Recovered Keys:')
for possible_address in recovered_keys:
    char = ' '
    if possible_address == address:
        char = '*'
    print(f' {char} {possible_address}')
verified_address = Wallet.Address.verify_address_signature(address, signature, message)
print(f'long address verified: {verified_address} ({address})')
address = address = wallet.public_address(False)
verified_address = Wallet.Address.verify_address_signature(address, signature, message)
print(f'short address verified: {verified_address} ({address})')

client = HTTPClient('https://test.confluxrpc.com')
print(json.dumps(client.getStatus(), indent=4))
