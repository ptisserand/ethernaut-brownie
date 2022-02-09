from brownie import accounts, PuzzleWallet, PuzzleProxy, interface, Wei

def main():
    owner = accounts[0]
    current = PuzzleWallet.deploy({'from': owner})
    data = current.init.encode_input(Wei('2 ether'))
    proxy = PuzzleProxy.deploy(owner, current, data, {'from': owner})
    wallet = interface.IPuzzleWallet(proxy)
    wallet.addToWhitelist(owner, {'from': owner})
    wallet.deposit({'from': owner, 'value': Wei('1 ether')})
    return {'proxy': proxy, 'owner': owner, 'wallet': wallet}


