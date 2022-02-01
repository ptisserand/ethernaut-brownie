// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface DenialInterface {
    function setWithdrawPartner(address _partner) external;

    function withdraw() external;
}
