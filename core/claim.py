import requests

from smart_airdrop_claimer import base
from core.headers import headers


def claim(token, proxies=None):
    url = "https://api.djdog.io/pet/collect?clicks=100000"

    try:
        response = requests.post(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        amount = data["data"]["amount"]
        return amount
    except:
        return None


def process_claim(token, proxies=None):
    amount = claim(token=token, proxies=proxies)
    if amount:
        base.log(
            f"{base.white}Auto Claim: {base.green}Success | Added {amount:,} coins"
        )
    else:
        base.log(f"{base.white}Auto Claim: {base.red}Fail")
