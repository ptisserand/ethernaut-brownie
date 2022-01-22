from brownie import Force, ForceAttack, accounts, Wei


def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    amount = Wei("0.01 ether")
    force = Force.deploy({'from': owner})
    assert force.balance() == 0
    attack = ForceAttack.deploy({'from': hacker})
    hacker.transfer(to=attack.address, amount=amount)
    assert attack.balance() == amount
    attack.destroy(force.address, {'from': hacker})
    assert attack.balance() == 0
    assert force.balance() == amount


