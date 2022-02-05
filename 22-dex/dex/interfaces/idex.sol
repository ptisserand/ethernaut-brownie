// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface IDex {
    function token1() external view returns(address);
    function token2() external view returns(address);
    function swap(address from, address to, uint amount) external;
    function get_swap_price(address from, address to, uint amount) external view returns(uint);
}