from brownie import Telephone, TelephoneAttack, accounts

def test_attack_change_owner():
    owner = accounts[0]
    hacker = accounts[1]
    telephone = Telephone.deploy({'from': owner})
    attack = TelephoneAttack.deploy(telephone.address,{'from': hacker})
    assert telephone.owner() != hacker
    attack.hack({'from': hacker})
    assert telephone.owner() == hacker
