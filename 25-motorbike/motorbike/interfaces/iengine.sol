// SPDX-License-Identifier: MIT

pragma solidity <0.7.0;

interface IEngine {
    function upgrader() external view returns (address);

    function horsePower() external view returns (uint256);

    function initialize() external;

    function upgradeToAndCall(address newImplementation, bytes memory data)
        external
        payable;
}
