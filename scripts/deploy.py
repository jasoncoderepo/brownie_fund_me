from brownie import FundMe,MockV3Aggregator,network, config
from scripts.helpful_scripts import get_account,deploy_mock,LOCAL_BLOCKCHAIN,FORK_MIANNET
from web3 import Web3
import time 



def deploy_fund_me():
    account = get_account()
    
    # 如果是部署在测试网，就传入相关的价格地址
    # 否则，就部署 mocks

    if network.show_active() not in LOCAL_BLOCKCHAIN or network.show_active() in FORK_MIANNET :
        print(network.show_active())
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        deploy_mock()  
        price_feed_address = MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(price_feed_address,{'from': account}, publish_source=config['networks'][network.show_active()].get('verify'))
    time.sleep(1)
    print(f'Contract deployed to {fund_me.address}')
    time.sleep(1)
    print(fund_me.getEntranceFee())
    return fund_me

def main():
    deploy_fund_me()

