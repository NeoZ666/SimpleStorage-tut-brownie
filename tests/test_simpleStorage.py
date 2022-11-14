from brownie import accounts, simpleStorage


# Arrange
# Act
# Assert
def test_deploy():
    # Arrange: Set up the stuff we are gonna use.
    account = accounts[0]
    contractObj = simpleStorage.deploy({"from": account})

    # Act: We will deploy the contract in acting stage.
    inital_value = contractObj.retrieve()
    expected = 0

    # Assert: Now test whether the actual output matches the expected value.
    assert inital_value == expected

def test_updatingStorage():
    # Arrange
    account = accounts[0]
    contractObj = simpleStorage.deploy({"from": account})

    # Act
    transaction = contractObj.store(20, {"from": account})
    transaction.wait(1)
    updated_value = contractObj.retrieve()
    expected = 20
    
    # Assert
    assert expected==updated_value