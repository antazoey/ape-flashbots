from ape.api import ProviderAPI, TransactionAPI, AccountAPI
from typing import List
from eth_account import Account, messages
from web3 import Web3, HTTPProvider
import json
import os
import requests


class FlashbotsProvider(ProviderAPI):
    # NOTE: delegate every other method to `self.upstream` (e.g. Infura)
    upstream: ProviderAPI

    def __post_init__(self):
        pass

    def send_bundle(self, bundle: List[TransactionAPI], sealer: AccountAPI):
        body = {"id": "0x" + os.urandom(4).hex(), "method": "eth_sendBundle", "params": [["0x" + txn.encode().hex() for txn in bundle], "0xB84969"]}
        message = messages.encode_defunct(text=Web3.keccak(text=json.dumps(body)).hex())
        sig = sealer.sign_message(message)
        result = requests.post("https://relay-goerli.flashbots.net", json=body, headers={'X-Flashbots-Signature': f"{sealer.address}:0x{sig.hex()}"})
        breakpoint()


