import requests

from smart_airdrop_claimer import base
from core.headers import headers


# 1: buy all available boxes
# 0: buy 1 box at a time
def box(token, proxies=None):
    url = f"https://api.djdog.io/pet/exchangeBox/1"

    try:
        response = requests.post(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        status = data["data"]
        return status
    except:
        return None


# 1: buy all available boosts
# 0: buy 1 boost at a time
def boost(token, proxies=None):
    url = f"https://api.djdog.io/pet/levelUp/1"

    try:
        response = requests.post(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        status = data["data"]
        return status
    except:
        return None


def process_buy_box(token, proxies=None):
    status = box(token=token, proxies=proxies)
    if status:
        base.log(
            f"{base.white}Auto Buy Box: {base.green}Success | Buy all available boxes"
        )
    else:
        base.log(
            f"{base.white}Auto Buy Box: {base.red}Fail | Not enough coin or Not eligible to buy"
        )


def process_buy_boost(token, proxies=None):
    status = boost(token=token, proxies=proxies)
    if status:
        base.log(
            f"{base.white}Auto Buy Boost: {base.green}Success | Buy all available boosts"
        )
    else:
        base.log(
            f"{base.white}Auto Buy Boost: {base.red}Fail | Not enough coin or Not eligible to buy"
        )
