# Add module top-level imports here
from ape import plugins
from .flashbots_provider import FlashbotsProvider


@plugins.register(plugins.ProviderPlugin)
def providers():
    yield "ethereum", "goerli", FlashbotsProvider
