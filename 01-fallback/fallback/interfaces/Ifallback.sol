// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface IFallback {
    function owner() external view returns(address payable);
    function contribute() external;
    function withdraw() external;
}