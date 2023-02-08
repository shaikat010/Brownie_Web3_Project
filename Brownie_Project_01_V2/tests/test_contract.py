from brownie import BasicContract, accounts

# While writing the test case functions, make sure you add the word “test” at the beginning of the function name.
# While running the tests, Brownie will ignore the functions that do not have the “test” prefix.

def test_default_value():
    # fetch the account
    account = accounts[0]
    # deploy contract
    deploy_contract = BasicContract.deploy({"from":account})
    #retrieve default number
    retrieved_number = deploy_contract.readNumber()
    expected_result = 0
    assert retrieved_number == expected_result

def test_stored_value():
    # fetch the account
    account = accounts[0]
    # deploy contract
    deploy_contract = BasicContract.deploy({"from":account})
    # store a number
    transaction_receipt = deploy_contract.storeNumber(1,{"from":account})
    transaction_receipt.wait(1)
    #retrieve number
    retrieved_number = deploy_contract.readNumber()
    expected_result = 1
    assert retrieved_number == expected_result