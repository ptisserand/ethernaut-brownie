from brownie import Token, accounts

def test_attack_overflow():
    owner = accounts[0]
    hacker = accounts[1]
    token = Token.deploy(1000000, {'from': owner})
    token.transfer(hacker, 20, {'from': owner})
    assert token.balanceOf(hacker) == 20
    token.transfer(hacker, 21, {'from': hacker})
    assert token.balanceOf(hacker) >= 20
