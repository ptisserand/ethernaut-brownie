# Elevator

## Objectif

L'objectif de ce challenge est d'atteindre le sommet du building

## Atteindre le sommet du building

Pour atteindre le sommet bu building, nous devons faire en sorte d'avoir `building.isLastFloor` qui retourne `false` à [la ligne 16](contracts/elevator.sol#16) et `true` à [la ligne 18](contracts/elevator.sol#18)

La méthode [`goTo`](contracts/elevator.sol#15) nécessite que le `msg.sender` respecte l'interface `Building`, nous devons donc faire en sorte que notre implémentation de `isLastFloor` ait ce comportement.

Nous voyons que dans le contrat `elevator` le [membre `floor` est modifié](contracts/elevator.sol#17) avant d'appeller de nouveau `isLastFloor`, nous pouvons nous appuyer sur le changement d'état de `floor` pour modifier notre valeur de retour de `isLastFloor` dans le contrat [`ElevatorAttack`](contracts/elevatorAttack.sol#14)

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0xaB4F3F2644060b2D960b0d88F0a42d1D27484687) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run scripts/attack.py main "0xb1ED8e7dfEc5CD1Ee2c587bf63EFd544819FFAa9" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

ElevatorProject is the active project.

Running 'scripts/attack.py::main'...
Transaction sent: 0xf7e7a20b3285ee6ec91e1c3b67d1c7f8ba7fc25bb0b926c36e2b25a6f5483969
  Gas price: 1.100000009 gwei   Gas limit: 188630   Nonce: 257
  ElevatorAttack.constructor confirmed   Block: 10545113   Gas used: 171482 (90.91%)
  ElevatorAttack deployed at: 0x63fb33696Abe1df90CC9c45c9042a96c7809A6c9

Transaction sent: 0x8c2cdd339f6e691e3b896430ca6ea20928ca7a77bd49410d7135d98b79493cb8
  Gas price: 1.100000009 gwei   Gas limit: 82121   Nonce: 258
  ElevatorAttack.attack confirmed   Block: 10545114   Gas used: 73944 (90.04%)

```




