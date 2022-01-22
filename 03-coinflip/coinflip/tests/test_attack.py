from brownie import CoinFlip, CoinFlipAttack, accounts

def test_attack_right_guess():
    coinflip = CoinFlip.deploy({'from': accounts[0]})
    attack = CoinFlipAttack.deploy(coinflip.address, {'from': accounts[1]})
    old = coinflip.consecutiveWins();
    for i in range(0, 10):
        attack.hack()
        nb = coinflip.consecutiveWins()
        assert nb == old + 1
        old = nb
    assert nb == 10
