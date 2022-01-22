pragma solidity ^0.6.0;

interface TokenInterface {
    function transfer(address _to, uint _value) external returns (bool);
    function balanceOf(address _owner) external view returns (uint balance);
}
