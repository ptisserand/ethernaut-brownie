// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

interface AlienCodexInterface {
    function owner() view external returns (address);

    function make_contact() external;

    function retract() external;

    function revise(uint256 i, bytes32 _content) external;
}
