from brownie import accounts, network, simpleStorage

def main():
    print(simpleStorage[0].retrieve())