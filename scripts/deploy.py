from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import deploy_mock, get_account, LOCAL_BLOCKCHAIN_ENV

def deploy_fund_me():
    account = get_account()
    #pass the price feed address to our contract 
    
    # if we are on persistent network like rinkeby, use the associated address 
    # otherwise deploy mocks 
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else: 
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address
      
    fund_me = FundMe.deploy(
        price_feed_address, 
        {"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")

    return fund_me

def main():
    deploy_fund_me()

    