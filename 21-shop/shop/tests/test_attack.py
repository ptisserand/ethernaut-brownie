from brownie import accounts, Shop, Buyer

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    shop = Shop.deploy({'from': owner})
    attack = Buyer.deploy(shop, {'from': hacker})
    ref_price = shop.price()
    attack.buy()
    assert shop.price() < ref_price
