from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN,FORK_MIANNET
from scripts.deploy import deploy_fund_me
import pytest
from brownie import network,accounts, exceptions


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrace_fee = fund_me.getEntranceFee() +100
    trans = fund_me.fund({'from' : account, 'value' : entrace_fee})
    trans.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrace_fee
    trans2 = fund_me.withdraw({'from' : account})
    trans2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN:
        pytest.skip('only for local testing')
    fund_me = deploy_fund_me()
    bad_actor = accounts[9]
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({'from' : bad_actor})