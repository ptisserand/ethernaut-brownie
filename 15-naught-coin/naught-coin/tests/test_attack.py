from brownie import accounts, NaughtCoin, NaughtCoinAttack

def test_attack():
    hacker = accounts[0]
    coin = NaughtCoin.deploy(hacker, {'from': hacker})
    assert coin.balanceOf(hacker) != 0
    hack = NaughtCoinAttack.deploy(coin, {'from': hacker})
    coin.approve(hack, coin.balanceOf(hacker), {'from': hacker})
    assert coin.allowance(hacker, hack) != 0
    hack.attack(hacker, {'from': hacker})
    assert coin.balanceOf(hacker) == 0
    hack.destroy({'from': hacker})
