pragma solidity ^0.6.0;

interface ReentranceInterface {
    function donate(address _to) external payable;

    function balanceOf(address _who) external view returns (uint256 balance);

    function withdraw(uint256 _amount) external;
}
