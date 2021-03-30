from .Util import keccak256, polymod, randomkey
import ecdsa
import re

class Wallet:
    acceptable_types = {'builtin': 0, 'user': 1, 'contract': 8 }
    def network_prefix_warning_string(network_prefix):
        return f'Network prefix of type "{network_prefix}" is invalid. It must either be "cfx", "cfxtest", or begin with "net" followed by and ending with a custom conflux network id number'
    def valid_network_prefix(network_prefix):
        return True if re.search('^(cfx|cfxtest|net[0-9]+)$', network_prefix) else False
    def random(type='user', network_prefix='cfx'):
        return Wallet(randomkey())
    def __init__(self, private_key, type='user', network_prefix='cfx'):
        if not Wallet.valid_network_prefix(network_prefix):
            raise Exception(Wallet.network_prefix_warning_string(network_prefix))
        if not Wallet.Address.is_valid_type(type):
            raise Exception(Wallet.Address.type_warning_string(type))
        self.type = type
        self.network_prefix = network_prefix
        self.private_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.verifying_key
    def public_address(self, include_type=True):
        return Wallet.Address.ptoa(self.public_key, self.type, self.network_prefix, include_type)
    def sign(self, message):
        return self.private_key.sign(message)
    class Address:
        acceptable_types = {'builtin': 0, 'user': 1, 'contract': 8 }
        acceptable_type_values = {0: 'builtin', 1: 'user', 8: 'contract' }
        base32_alphabet = 'abcdefghjkmnprstuvwxyz0123456789'
        def is_valid_type(type):
            return type in Wallet.Address.acceptable_types
        def type_warning_string(type):
            return f'Wallet of type "{type}" is not acceptable. Wallet type must be one of {", ".join([key for key in Wallet.Address.acceptable_types])}'
        def htoa(public_key_hex, type, network_prefix, include_type=True):
            print(public_key_hex)
            _binary = '00000000' + bin(int(public_key_hex, base=16))[2:].zfill(160) + '00'
            _chunks = [int(_binary[i:i+5], 2) for i in range(0, len(_binary), 5)]
            _base32 = ''.join([Wallet.Address.base32_alphabet[position] for position in _chunks])
            _checksum = bin(polymod([byte & 31 for byte in bytes(network_prefix, 'ascii')] + [0] + _chunks + [0, 0, 0, 0, 0, 0, 0, 0]))[2:].zfill(40)
            _chunks = [int(_checksum[i:i+5], 2) for i in range(0, len(_checksum), 5)]
            _checksum = ''.join([Wallet.Address.base32_alphabet[position] for position in _chunks])
            return (f'{network_prefix}:type.{type}' if include_type else network_prefix) + f':{_base32}{_checksum}'
        def ptoa(public_key, type, network_prefix, include_type=True):
            if not Wallet.Address.is_valid_type(type):
                raise Exception(Wallet.Address.type_warning_string(type))
            return Wallet.Address.htoa(f'{Wallet.Address.acceptable_types[type]}' + keccak256(public_key.to_string())[-39:], type, network_prefix, include_type)
        def __init__(self, address):
            if address.lower() != address:
                raise Exception('Wallet address is not in lowercase format. Rejecting as per CIP-37 specification')
            split = address.split(':')
            if len(split) < 2:
                raise Exception('Wallet address does not contain network prefix. Rejecting as per CIP-37 specification')
            self.network_prefix = split[0]
            if not Wallet.valid_network_prefix(self.network_prefix):
                raise Exception(Wallet.network_prefix_warning_string(self.network_prefix))
            _payload_raw = [Wallet.Address.base32_alphabet.index(char) for char in split[len(split) - 1]]
            _checksum = polymod([byte & 31 for byte in bytes(self.network_prefix, 'ascii')] + [0] + _payload_raw)
            if _checksum != 0:
                 raise Exception('Wallet address checksum validation failed. Invalid address was supplied')
            _binary = ''.join([bin(int)[2:].zfill(5) for int in _payload_raw])
            _address_type = int(_binary[8:12], 2)
            if _address_type not in Wallet.Address.acceptable_type_values:
                 raise Exception('Address type of value {_address_type} unknown. Input is rejected')
            self.type =  Wallet.Address.acceptable_type_values[_address_type]
            _address_size = 160 + (32 * int(_binary[4:8]))
            self.address = bytes([int(_binary[i * 8:(i+1)*8], 2) for i in range(1, int(_address_size / 8) + 1)])
        def get_address(self):
            return Wallet.Address.htoa(self.address.hex(), self.type, self.network_prefix)
