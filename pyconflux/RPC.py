from .Util import randomkey
import json
import requests

def translate_param(param):
    if is_instance(param, int):
        return '0' + hex(value).lstrip('0').zfill(1)
    if is_instance(param, bytes):
        return '0x' + param.hex()
    if is_instance(param, list):
        return [ translate_param(_param) for _param in param ]
    if is_instance(param, dict):
        return { _param: translate_param(param[_param]) for _param in param }
    return param

class HTTPClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.id = 0
    def request(self, method, params=None):
        data = {
            'jsonrpc': '2.0',
            'method': method,
        }
        if params != None:
            data['params'] = params
        self.id = self.id + 1
        data['id'] = self.id
        response = requests.post(self.endpoint, json = data)
        response.raise_for_status()
        return response.json()
    def getTransactionByHash(self, transaction_hash):
        return self.request('cfx_getTransactionByHash', [transaction_hash])
    def getBlockByHash(self, block_hash, full_transactions):
        return self.request('cfx_getBlockByHash', [block_hash, full_transactions])
    def getBlockByEpochNumber(self, epoch, full_transactions):
        return self.request('cfx_getBlockByEpochNumber', [epoch, full_transactions])
    def getBestBlockHash(self):
        return self.request('cfx_getBlockByEpochNumber')
    def epochNumber(self, epoch='latest_mined'):
        return self.request('cfx_epochNumber', [epoch])
    def gasPrice(self):
        return self.request('cfx_gasPrice')
    def getBlocksByEpoch(self, epoch):
        return self.request('cfx_getBlocksByEpoch', [epoch])
    def getBalance(self, address, epoch='latest_state'):
        return self.request('cfx_getBalance', [address, epoch])
    def getStakingBalance(self, address, epoch='latest_state'):
        return self.request('cfx_getStakingBalance', [address, epoch])
    def getCollateralForStorage(self, address, epoch='latest_state'):
        return self.request('cfx_getCollateralForStorage', [address, epoch])
    def getAdmin(self, address, epoch='latest_state'):
        return self.request('cfx_getAdmin', [address, epoch])
    def getCode(self, address, epoch='latest_state'):
        return self.request('cfx_getCode', [address, epoch])
    def getStorageAt(self, address, storage_position, epoch='latest_state'):
        return self.request('cfx_getStorageAt', [address, storage_position, epoch])
    def getStorageRoot(self, address, epoch='latest_state'):
        return self.request('cfx_getStorageRoot', [address, epoch])
    def getSponsorInfo(self, address, epoch='latest_state'):
        return self.request('cfx_getSponsorInfo', [address, epoch])
    def getNextNonce(self, address, epoch='latest_state'):
        return self.request('cfx_getNextNonce', [address, epoch])
    def sendRawTransaction(self, signed_transaction):
        return self.request('cfx_sendRawTransaction', [signed_transaction])
    def call(self, address_from=None, address_to=None, gas_price=0, gas=500000000, value=0, data='0x', nonce=0, epoch='latest_state'):
        return self.request(
            'cfx_call',
            [{
                'from': address_from,
                'to': address_to,
                'data': data,
                'gasPrice': gas_price,
                'nonce': nonce
            }],
            epoch
        )
    def estimateGasAndCollateral(self, address_from=None, address_to=None, gas_price=0, gas=500000000, value=0, data='0x', nonce=0, epoch='latest_state'):
        return self.request(
            'cfx_call',
            [{
                'from': address_from,
                'to': address_to,
                'data': data,
                'gasPrice': gas_price,
                'nonce': nonce
            }, epoch]
        )
    def getLogs(self, from_epoch='latest_checkpoint', to_epoch='latest_state', block_hashes=None, address=None, topics=None, limit=None):
        return self.request(
            'cfx_getLogs',
            [{
                'fromEpoch': from_epoch,
                'toEpoch': to_epoch,
                'address': address,
                'topics': topics,
                'limit': nonce
            } if block_hashes is not None else {
                'block_hashes': block_hashes,
                'address': address,
                'topics': topics,
                'limit': nonce
            }]
        )
    def getTransactionReceipt(self, transaction_hash):
        return self.request(
            'cfx_getTransactionReceipt',
            [transaction_hash]
        )
    def getAccount(self, address):
        return self.request('cfx_getAccount', [address, epoch])
    def getInterestRate(self, epoch):
        return self.request('cfx_getInterestRate', [epoch])
    def getAccumulateInterestRate(self, epoch):
        return self.request('cfx_getAccumulateInterestRate', [epoch])
    def checkBalanceAgainstTransaction(self, account_address, contract_address, gas_limit, gas_price, storage_limit, epoch):
        return self.request('cfx_checkBalanceAgainstTransaction', [account_address, contract_address, gas_limit, gas_price, storage_limit, epoch])
    def getSkippedBlocksByEpoch(self, epoch):
        return self.request('cfx_getSkippedBlocksByEpoch', [epoch])
    def getConfirmationRiskByHash(self, block_hash):
        return self.request('cfx_getConfirmationRiskByHash', [block_hash])
    def getStatus(self):
        return self.request('cfx_getStatus')
    def clientVersion(self):
        return self.request('cfx_clientVersion')
    def getBlockRewardInfo(self, epoch):
        return self.request('cfx_getBlockRewardInfo', epoch)
    def getBlockByHashWithPivotAssumption(self, block_hash, pivot_hash, epoch):
        return self.request('cfx_getBlockByHashWithPivotAssumption', [block_hash, pivot_hash, epoch])
    def getDepositList(self, address, epoch):
        return self.request('cfx_getDepositList', [address, epoch])
    def getVoteList(self, address, epoch):
        return self.request('cfx_getVoteList', [address, epoch])
