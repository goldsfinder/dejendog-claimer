import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = f"https://api.djdog.io/telegram/login?{data}"

    try:
        response = requests.get(url=url, headers=headers(), proxies=proxies, timeout=20)
        data = response.json()
        token = data["data"]["accessToken"]
        return token
    except:
        return None
