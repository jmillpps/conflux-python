from Crypto.Hash import keccak
import os
import ecdsa

def keccak256(input):
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(input)
    return keccak_hash.hexdigest()

def polymod(values):
    c = 1
    for d in values:
        c0 = c >> 35
        c = ((c & 0x07ffffffff) << 5) ^ d
        if (c0 & 0x01):
            c ^= 0x98f2bc8e61
        if (c0 & 0x02):
            c ^= 0x79b76d99e2
        if (c0 & 0x04):
            c ^= 0xf33e5fb3c4
        if (c0 & 0x08):
            c ^= 0xae2eabe2a8
        if (c0 & 0x10):
            c ^= 0x1e4f43e470
    return c ^ 1

def randomkey(bytes=32):
    return os.urandom(bytes)
