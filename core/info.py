import requests

from smart_airdrop_claimer import base
from core.headers import headers


def user_info(token, proxies=None):
    url = "https://api.djdog.io/userCenter/information"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        level = data["data"]["level"]
        hsk = data["data"]["hskAmount"]
        invite_num = data["data"]["inviteNum"]
        valid_invite_num = data["data"]["validInviteNum"]
        base.log(
            f"{base.green}Level: {base.white}{level} - {base.green}HSK: {base.white}{hsk} - {base.green}Friends: {base.white}{invite_num} - {base.green}Eligible friends: {base.white}{valid_invite_num}"
        )
        return data
    except:
        return None


def pet_info(token, proxies=None):
    url = "https://api.djdog.io/pet/barAmount"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        gold = data["data"]["goldAmount"]
        claimable = data["data"]["availableAmount"]
        bar_limit = data["data"]["barGoldLimit"]
        base.log(
            f"{base.green}Gold: {base.white}{gold:,} - {base.green}Claimable: {base.white}{claimable:,} - {base.green}Bar limit: {base.white}{bar_limit:,}"
        )
        return data
    except:
        return None


def box_info(token, proxies=None):
    url = "https://api.djdog.io/pet/boxMall"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        box = data["data"]["boxAmount"]
        buy_box_limit = data["data"]["boxBuyLimit"]
        boost_limit = data["data"]["boostLimit"]
        base.log(
            f"{base.green}Box: {base.white}{box} - {base.green}Available Box to Buy: {base.white}{buy_box_limit} - {base.green}Available Level to Boost: {base.white}{boost_limit}"
        )
        return buy_box_limit, boost_limit
    except:
        return None


def get_info(token, proxies=None):
    user_info(token=token, proxies=proxies)
    pet_info(token=token, proxies=proxies)
    box_info(token=token, proxies=proxies)
