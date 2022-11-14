from brownie import accounts, config, simpleStorage, network
import os

#this works for local env like ganache cuz brownie launches an instance of ganache with it's private keys(so we don't need to specify them) and we just need to give one address.
def interactions():

    account = selectAccount()
    # When we deploy the contract and use .transact, use from:address, but while .call them, we need not mention the acc since we aren't making any state changes.
    contractObj = simpleStorage.deploy({"from": account})
    initial_storedValue = contractObj.retrieve()
    print(initial_storedValue)
    transaction = contractObj.store(15, {"from": account})
    transaction.wait(1)
    updated_storedValue = contractObj.retrieve()
    print(updated_storedValue)

def selectAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
        
#Working with testnet is a bit different in brownie. Here, we use cmd line and add a new acc natively to brownie.
#After that, u will export ur pvt key from metamask(testnet wala) and it will actually ask for a password and create a new account. Pretty amazing, ik.

def main():
    interactions()