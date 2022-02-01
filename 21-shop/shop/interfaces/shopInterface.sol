// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface ShopInterface {
  function price() external view returns (uint);
  function isSold() external view returns (bool);
  function buy() external;
}
