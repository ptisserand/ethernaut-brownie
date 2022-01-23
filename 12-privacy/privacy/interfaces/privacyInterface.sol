// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface PrivacyInterface {
    function locked() external view returns(bool);
    function unlock(bytes16 _key) external;
}