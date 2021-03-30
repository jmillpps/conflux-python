from src.Wallet import Wallet
import os

wallet = Wallet(private_key=os.urandom(32), type='user', network_prefix='cfx')
print(f'wallet address: {wallet.public_address()}')
addr = Wallet.Address(wallet.public_address())
print(f'addr address: {addr.get_address()}')
