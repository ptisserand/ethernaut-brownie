// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface PreservationInterface {
    function owner() external pure returns(address);
    function setFirstTime(uint _timeStamp) external;
}
