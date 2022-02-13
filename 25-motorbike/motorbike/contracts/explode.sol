// SPDX-License-Identifier: MIT

pragma solidity <0.7.0;

contract Boom {
    constructor() public {}

    function explode() public {
        selfdestruct(msg.sender);
    }
}
