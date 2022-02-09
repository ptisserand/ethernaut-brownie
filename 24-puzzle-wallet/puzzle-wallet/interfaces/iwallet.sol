// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

interface IPuzzleProxy  {
    function admin() view external returns(address);
    function proposeNewAdmin(address _newAdmin) external;
}

interface IPuzzleWallet {
    function owner() view external returns(address);
    function setMaxBalance(uint256 _maxBalance) external;
    function addToWhitelist(address addr) external;
    function deposit() external payable;
    function execute(address to, uint256 value, bytes calldata data) external payable;
    function multicall(bytes[] calldata data) external payable;
}
