from brownie import accounts, interface, GateKeeperTwo, GateKeeperTwoAttack

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    gate = GateKeeperTwo.deploy({'from': owner})
    attack = GateKeeperTwoAttack.deploy(gate, {'from': hacker})
    assert gate.entrant() == hacker.address
