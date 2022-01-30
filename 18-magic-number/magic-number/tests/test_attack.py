from brownie import accounts, web3, interface, Dummy

# Return 42 whatever the call
# Store 42 in memory at position 0x40
# 602a: PUSH1 0x2a
# 6040: PUSH1 0x40
# 52: MSTORE
# 6020: PUSH1 0x20 // value is 32 bytes in size
# 6040: PUSH1 0x40  
# F3: RETURN

# Constructor
# 600a: PUSH1 0x0a // 10 bytes size of our runtime
# 600c: PUSH1 0x0c // where our runtime will be located
# 6000: PUSH1 0x00 // destination copy
# 39: CODECOPY // copy runtime
# 600a: PUSH1 0x0a // runtime size
# 6000: PUSH1 0x00 // runtime location
# F3: RETURN
# Total initialization size is 12 bytes 

# Final sequence
# 600a600c600039600a6000f3604260405260206040f3

def test_attack():
    hacker = accounts[0]
    bytecode = "0x600a600c600039600a6000f3602a60405260206040f3"
    Meaning = Dummy
    Meaning.bytecode = bytecode
    meaning = Meaning.deploy({'from': hacker})
    check = interface.CheckInterface(meaning)
    assert 42 == check.whatIsTheMeaningOfLife()

