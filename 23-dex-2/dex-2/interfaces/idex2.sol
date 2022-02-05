// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface IDexTwo {
    function token1() view external returns(address);
    function token2() view external returns(address);
    function swap(
        address from,
        address to,
        uint256 amount
    ) external;

    function add_liquidity(address token_address, uint256 amount) external;
}
