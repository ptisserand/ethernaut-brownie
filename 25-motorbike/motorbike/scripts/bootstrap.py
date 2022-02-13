from brownie import accounts, Motorbike, Engine

def main():
    owner = accounts[0]
    admin = accounts[1]
    engine = Engine.deploy({'from': owner})
    motorbike = Motorbike.deploy(engine, {'from': admin})
    return {'owner': owner, 'admin': admin, 'engine': engine, 'motorbike': motorbike}
