from brownie import accounts, GateKeeperOne, GateKeeperAttack


def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    print(hacker.balance())
    gate = GateKeeperOne.deploy({'from': owner})
    attack = GateKeeperAttack.deploy(gate.address, {'from': hacker})
    tx = attack.attack(200, {'from': hacker})
    assert len(tx.events) > 0
    print(tx.events[0])

