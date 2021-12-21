import json
import os
from typing import List, Optional

import requests  # type: ignore
from ape.api import (
    AccountAPI,
    ConfigItem,
    ProviderAPI,
    TransactionAPI,
    UpstreamProvider,
    Web3Provider,
)
from eth_account import messages
from web3 import HTTPProvider, Web3


class FlashbotsConfig(ConfigItem):
    upstream: Optional[str] = None


class FlashbotsProvider(Web3Provider, ProviderAPI):
    def connect(self):
        upstream_provider_name = self.config.upstream

        # TODO: Handle "network name" selection (goerli or mainnet, reject others)
        # HINT: use `self.network.name`
        if upstream_provider_name:
            upstream_provider = self.network.ecosystem.goerli.get_provider(
                provider_name=upstream_provider_name
            )
        else:
            upstream_provider = self.network.ecosystem.goerli.default_provider

        if not isinstance(upstream_provider, UpstreamProvider):
            raise Exception("Not upstreamable!")

        self._web3 = Web3(HTTPProvider(upstream_provider.connection_str))
        if not self._web3.isConnected():
            raise Exception("Not active!")

    def disconnect(self):
        self._web3 = None

    def send_bundle(self, bundle: List[TransactionAPI], sealer: AccountAPI):
        body = {
            "id": "0x" + os.urandom(4).hex(),
            "method": "eth_sendBundle",
            "params": [["0x" + txn.encode().hex() for txn in bundle], "0xB84969"],
        }
        # TODO: The format of `json.dumps(body)` is wrong, leading to auth bug w/ flashbots server
        message = messages.encode_defunct(
            text=Web3.keccak(text=json.dumps(body, separators=(",", ":"), sort_keys=True)).hex()
        )
        sig = sealer.sign_message(message)
        if not sig:
            raise Exception("user did not sign")

        result = requests.post(  # noqa: F841
            "https://relay-goerli.flashbots.net",
            json=body,
            headers={"X-Flashbots-Signature": f"{sealer.address}:0x{sig.encode_vrs().hex()}"},
        )
