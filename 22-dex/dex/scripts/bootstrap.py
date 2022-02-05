from brownie import accounts, Dex, SwappableToken

def main():
    owner = accounts[0]
    hacker = accounts[1]
    token1 = SwappableToken.deploy('Token1', 'TKN1', 1000, {'from': owner})
    token2 = SwappableToken.deploy('Token2', 'TKN2', 1000, {'from': owner})
    dex = Dex.deploy(token1, token2, {'from': owner})
    token1.transfer(dex, 100, {'from': owner})
    token2.transfer(dex, 100, {'from': owner})
    token1.transfer(hacker, 10, {'from': owner})
    token2.transfer(hacker, 10, {'from': owner})
    token1.approve(dex, 1000, {'from': hacker})
    token2.approve(dex, 1000, {'from': hacker})
    return {'hacker': hacker, 'owner': owner, 'token1': token1, 'token2': token2, 'dex': dex}

