// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface GateKeeperTwoInterface {
    function entrant() external pure returns (address);
    function enter(bytes8) external returns (bool);
}