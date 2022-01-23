// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface ElevatorInterface {
    function floor() external returns (uint);
    function goTo(uint256 _floor) external;
}
