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
git clone https://github.com/unparalleled-js/ape-flashbots
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
$ git remote set-url origin git@github.com:<your_account>/<repo>.git
```
#### set your upstream version [main branch example]
```
$ git remote add upstream git@github.com:ApeWorx/ape.git
```
#### add an available remote from PR
```
$ git remote add <branch> git@github.com:<branch>/<repo>.git
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
$ ape accounts generate <account-name>
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
In [1]: a = accounts.load("<account-name>")
```
#### send the bundle
```
In [2]: networks.active_provider.send_bundle([], a)
SignableMessage(version=b'E', header=b'thereum Signed Message:\n66', body=b'<key>')

Sign:  [y/N]: y
Enter Passphrase to unlock '<your-account>' []: 
Leave '<your-account>' unlocked? [y/N]: y
--Return--
> /directory/to/ape-flashbots/ape_flashbots/providers.py(64)send_bundle()->None
-> breakpoint()
```
```
(Pdb) result.text
'{"error":{"message":"signer address does not equal expected, got 0x8bC1de9A15e511b42dDcD8A6309cbCd2E42EAAdd, expected <your-secret-key>"}}'
(Pdb) exit
```
## currently have an issue with key conversion in send_bundle

## Development

This project is in early development and should be considered an alpha.
Things might not work, breaking changes are likely.
Comments, questions, criticisms and pull requests are welcomed.

## License

This project is licensed under the [Apache 2.0](LICENSE).
