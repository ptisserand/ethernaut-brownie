import pytest 

from brownie import run

def test_attack(accounts):
    ret = run('bootstrap.py')
    wallet = ret['wallet']
    proxy = ret['proxy']
    owner = ret['owner']
    hacker = accounts[1]
    ### attack start here
    assert owner != hacker
    run('attack.py', method_name="become_owner", args=[proxy.address, hacker])
    assert wallet.owner() == hacker
    run('attack.py', method_name="withdraw", args=[proxy.address, hacker])
    assert wallet.balance() == 0
    run('attack.py', method_name="become_admin", args=[proxy.address, hacker])
    assert proxy.admin() == hacker


    