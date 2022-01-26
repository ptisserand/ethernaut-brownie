from brownie import accounts, config, GateKeeperTwoAttack, interface

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    hack = GateKeeperTwoAttack.deploy(target, {'from': hacker})
    gate = interface.GateKeeperTwoInterface(target)
    print(f'Entrant: {gate.entrant()}')


