from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    create_collectible_tx = simple_collectible.createCollectible(
        sample_token_uri, {"from": account}
    )
    create_collectible_tx.wait(1)
    print(
        f"Great stuff. View the NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() -1 )}"
    )  # -1 for the most recently deployed one
    print("Wait up to 20mins, then hit the refresh metadata button.")
    return simple_collectible


def main():
    deploy_and_create()
