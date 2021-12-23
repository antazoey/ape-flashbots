# Ape Flashbots

TODO: Description

## Dependencies

* [python3](https://www.python.org/downloads) version 3.7 or greater, python3-dev

## Installation

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape_flashbots
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-flashbots.git
cd ape_flashbots
python3 setup.py install
```

## Environment Setup

#### check available remotes
```
$ git remote -V
```
#### set your origin for your Pull Request
```
$ git remote set-url origin git@github.com:johnson2427/ape.git
```
#### set your upstream version [main branch]
```
$ git remote add upstream git@github.com:ApeWorx/ape.git
```
#### add an available remote from PR
```
$ git remote add <branch> git@github.com:<branch>/ape.git
```

## Quick Usage

#### Setup dev environment
```
$ pip install -e .[dev]
```

#### Check config
```
$ ape --config
```

#### Install ape plugins
```
$ ape plugins install
```

#### If WEB3_INFURA_API_KEY is NOT in your environment [for goerli]
```
$ WEB3_INFURA_API_KEY=<your-api-key>
$ export WEB3_INFURA_API_KEY
```

#### Generate account

```
$ ape accounts generate johnson_test
```

#### Install ape -> branch from bryant

```
$ pip install ../ape
```

#### start the plugin:
```
$ ape console --network :goerli:flashbots
```
#### setup your account
```
In [1]: a = accounts.load("johnson_test")
```
#### send the bundle
```
In [2]: networks.active_provider.send_bundle([], a)
SignableMessage(version=b'E', header=b'thereum Signed Message:\n66', body=b'0x7060d9ac9abe450a7fd5ad2f62c34e81f6af446aa88f1e0c9e9392b3a53dc089')

Sign:  [y/N]: y
Enter Passphrase to unlock 'johnson_test' []: 
Leave 'johnson_test' unlocked? [y/N]: y
--Return--
> /home/blake/ApeWorx/ape-flashbots/ape_flashbots/providers.py(64)send_bundle()->None
-> breakpoint()
```
```
(Pdb) result.text
'{"error":{"message":"signer address does not equal expected, got 0x8bC1de9A15e511b42dDcD8A6309cbCd2E42EAAdd, expected 0x5ab1f67Da42F71E52b88d9d32570b58a28042611"}}'
(Pdb) exit
```
## currently have an issue with key conversion in send_bundle

## Development

This project is in early development and should be considered an alpha.
Things might not work, breaking changes are likely.
Comments, questions, criticisms and pull requests are welcomed.

## License

This project is licensed under the [Apache 2.0](LICENSE).
