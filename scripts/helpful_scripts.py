from brownie import network, accounts, config,MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARING_VALUE = 200000000000
FORK_MIANNET = 'mainnet-fork-dev'
LOCAL_BLOCKCHAIN =['development', 'ganache-local']

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN or network.show_active() in FORK_MIANNET:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
    
def deploy_mock():
    print(f'The active networks is {network.show_active()}')
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARING_VALUE, {'from': get_account()})
    print("Mock Deloyed!") 
 