// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'interfaces/shopInterface.sol';

contract Buyer {
    bool first = true;
    ShopInterface shop;

    constructor(address _address) public {
        shop = ShopInterface(_address);
    }

    function price() public returns(uint) {
        uint ref_price = shop.price();
        if (!shop.isSold()) {
            return ref_price + 10;
        } else {
            return ref_price - 10;
        }
    }

    function buy() public {
        shop.buy();
    }
}
