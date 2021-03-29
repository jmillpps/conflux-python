from .Util import keccak256, polymod, randomkey
import ecdsa

class Wallet:
    acceptable_types = {'builtin': 0, 'user': 1, 'contract': 8 }
    def random(type='user', network_prefix='cfx'):
        if not Wallet.Address.is_valid_type(type):
            raise Exception(Wallet.Address.type_warning_string(type))
        return Wallet(randomkey())
    def __init__(self, private_key, type='user', network_prefix='cfx'):
        self.type = type
        self.network_prefix = network_prefix
        self.private_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.verifying_key
    def public_address(self, include_type=True):
        return Wallet.Address.ptoa(self.public_key, self.type, self.network_prefix, include_type)
    class Address:
        acceptable_types = {'builtin': '0', 'user': '1', 'contract': '8' }
        base32_alphabet = 'abcdefghjkmnprstuvwxyz0123456789'
        def is_valid_type(type):
            return type in Wallet.Address.acceptable_types
        def type_warning_string(type):
            return 'Wallet of type "{type}" is not acceptable. Wallet type must be one of {", ".join([key for key in Wallet.Address.acceptable_types])}'
        def ptoa(public_key, type, network_prefix, include_type=True):
            if not Wallet.Address.is_valid_type(type):
                raise Exception(Wallet.Address.type_warning_string(type))
            _hex = f'{Wallet.Address.acceptable_types[type]}' + keccak256(public_key.to_string())[-39:]
            _binary = '00000000' + bin(int(_hex, base=16))[2:].zfill(160) + '00'
            _chunks = [int(_binary[i:i+5], 2) for i in range(0, len(_binary), 5)]
            _base32 = ''.join([Wallet.Address.base32_alphabet[position] for position in _chunks])
            _checksum = bin(polymod([byte & 31 for byte in bytes(network_prefix, 'ascii')] + [0] + _chunks + [0, 0, 0, 0, 0, 0, 0, 0]))[2:].zfill(40)
            _chunks = [int(_checksum[i:i+5], 2) for i in range(0, len(_checksum), 5)]
            _checksum = ''.join([Wallet.Address.base32_alphabet[position] for position in _chunks])
            return (f'{network_prefix}:type.{type}' if include_type else network_prefix) + f':{_base32}{_checksum}'
