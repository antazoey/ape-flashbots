# Add module top-level imports here
from ape import plugins

from .providers import FlashbotsConfig, FlashbotsProvider


@plugins.register(plugins.Config)
def config_class():
    return FlashbotsConfig


@plugins.register(plugins.ProviderPlugin)
def providers():
    yield "ethereum", "goerli", FlashbotsProvider
