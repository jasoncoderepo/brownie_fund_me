from brownie import FundMe
from scripts.helpful_scripts import get_account
from web3 import Web3


def fund():
    fund_me = FundMe[-1]
    account =  get_account()
    enteance_fee = fund_me.getEntranceFee()
    print(enteance_fee)
    print(f'The Current entry fee is {enteance_fee}')
    print("Funding")
    fund_me.fund({'from' : account, "value" : Web3.toWei(1, 'ether')})
    # fund_me.wait(1)
    print(fund_me.addressToAmountFunded(account))

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({'from' : account, 'gasLimit' : 10000000000})
    # print(fund_me.balance())


def main():
    fund()
    withdraw()
