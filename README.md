# conflux-python
## Python toolkit for interfacing with the Conflux protocol

conflux-python is a python-based implementation of Conflux protocol

## Features
- Wallet
  - Generate Public / Private Keys
  - Sign And Verify Signatures
  - Recover Public Keys From Signatures
  - Verify Address Matching Recovered Public Key From Signed Message Signature
- RPC
  - All RPC methods described by https://conflux-chain.github.io/conflux-doc/json-rpc/ as of 2021-04-07 are available

## Example (generate_wallet.py):

$ python3 generate_wallet.py
Wallet Address: cfx:type.user:aark79pfpv18hpns77vfmv53bgptpj1zajvhdewada
Old Wallet Address: 0x1a9efd85646fe3b16eef625547790998f622f502
Test Message: b'Message for ECDSA signing'
Signature: 23cbd6e1a60f0044df9945b6be33d5e2ea62a827bbceeaebbb1591d0afdd8b160f335e04cdbd628bcdfa247766ee3c5c2b38496c32cf498094a1b2627bee8d0c
Recovered Keys:
 * cfx:type.user:aark79pfpv18hpns77vfmv53bgptpj1zajvhdewada
   cfx:type.user:aaky7h72yh58rrv7azje1bb5nve5ybzt6ufb6pgx21
long address verified: True (cfx:type.user:aark79pfpv18hpns77vfmv53bgptpj1zajvhdewada)
short address verified: False (cfx:aark79pfpv18hpns77vfmv53bgptpj1zajvhdewada)
{
    "jsonrpc": "2.0",
    "result": {
        "bestHash": "0xbca56b4763c4597f15a1df56f444f9d094d930bf96fa0eae5150e45fa27f96af",
        "blockNumber": "0x198515d",
        "chainId": "0x1",
        "epochNumber": "0x1431e8e",
        "latestCheckpoint": "0x140bd60",
        "latestConfirmed": "0x1431e4e",
        "latestState": "0x1431e8a",
        "networkId": "0x1",
        "pendingTxNumber": "0x32"
    },
    "id": 1
}
