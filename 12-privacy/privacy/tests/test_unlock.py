import secrets
from brownie import accounts, web3, Privacy


def test_unlock():
    target = Privacy.deploy(
        [secrets.token_bytes(32), secrets.token_bytes(32), secrets.token_bytes(32)],
        {"from": accounts[0]},
    )
    # retrieve data
    data = [
        web3.eth.get_storage_at(target.address, 3),
        web3.eth.get_storage_at(target.address, 4),
        web3.eth.get_storage_at(target.address, 5),
    ]
    long_key = data[2]
    assert target.locked() == True
    target.unlock(long_key[:16], {'from': accounts[1]})
    assert target.locked() == False

