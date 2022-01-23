from brownie import accounts, Elevator, ElevatorAttack

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    target = Elevator.deploy({'from': owner})
    hack = ElevatorAttack.deploy(target, {'from': hacker})
    assert target.floor() == 0
    assert target.top() == False
    hack.attack(10, {'from': hacker})
    assert target.top() == True
