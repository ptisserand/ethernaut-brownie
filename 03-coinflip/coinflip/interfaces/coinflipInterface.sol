pragma solidity ^0.6.0;

interface CoinFlipInterface {
    function flip(bool _guess) external returns (bool);
}

