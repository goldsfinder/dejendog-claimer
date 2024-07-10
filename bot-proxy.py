import os
import sys
import time
import requests
from colorama import *
from datetime import datetime
import random
import json

red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the full paths to the files
data_file = os.path.join(script_dir, "data-proxy.json")


class DejenDog:
    def __init__(self):

        self.line = white + "~" * 50

        self.banner = f"""
        {blue}Smart Airdrop {white}DejenDog Auto Claimer
        t.me/smartairdrop2120
        
        """

    def headers(self, auth_data):
        return {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": f"{auth_data}",
            "Cache-Control": "no-cache",
            "Origin": "https://djdog.io",
            "Pragma": "no-cache",
            "Priority": "u=1, i",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }

    def proxies(self, proxy_info):
        return {"http": f"{proxy_info}", "https": f"{proxy_info}"}

    # Clear the terminal
    def clear_terminal(self):
        # For Windows
        if os.name == "nt":
            _ = os.system("cls")
        # For macOS and Linux
        else:
            _ = os.system("clear")

    def login(self, data, proxy_info):
        url = f"https://api.djdog.io/telegram/login?{data}"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Origin": "https://djdog.io",
            "Pragma": "no-cache",
            "Priority": "u=1, i",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.get(url=url, headers=headers, proxies=proxies)

        return response

    def user_info(self, auth_data, proxy_info):
        url = f"https://api.djdog.io/pet/barAmount"

        headers = self.headers(auth_data=auth_data)

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.get(url, headers=headers, proxies=proxies)

        return response

    def submit_click(self, auth_data, click, proxy_info):
        url = f"https://api.djdog.io/pet/collect?clicks={click}"

        headers = self.headers(auth_data=auth_data)

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url, headers=headers, proxies=proxies)

        return response

    def log(self, msg):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{black}[{now}]{reset} {msg}{reset}")

    def parse_proxy_info(self, proxy_info):
        try:
            stripped_url = proxy_info.split("://", 1)[-1]
            credentials, endpoint = stripped_url.split("@", 1)
            user_name, password = credentials.split(":", 1)
            ip, port = endpoint.split(":", 1)
            return {"user_name": user_name, "pass": password, "ip": ip, "port": port}
        except:
            return None

    def main(self):
        while True:
            self.clear_terminal()
            print(self.banner)
            accounts = json.load(open(data_file, "r"))["accounts"]
            num_acc = len(accounts)
            self.log(self.line)
            self.log(f"{green}Numer of account: {white}{num_acc}")
            for no, account in enumerate(accounts):
                self.log(self.line)
                self.log(f"{green}Account number: {white}{no+1}/{num_acc}")
                data = account["acc_info"]
                proxy_info = account["proxy_info"]
                parsed_proxy_info = self.parse_proxy_info(proxy_info)
                if parsed_proxy_info is None:
                    self.log(
                        f"{red}Check proxy format: {white}http://user:pass@ip:port"
                    )
                    break
                ip_adress = parsed_proxy_info["ip"]
                self.log(f"{green}IP Address: {white}{ip_adress}")

                try:
                    login = self.login(data=data, proxy_info=proxy_info).json()
                    auth_data = login["data"]["accessToken"]
                    user_info = self.user_info(
                        auth_data=auth_data, proxy_info=proxy_info
                    ).json()
                    hit_available = user_info["data"]["availableAmount"]
                    balance = user_info["data"]["goldAmount"]
                    self.log(f"{green}Balance: {white}{balance:,}")
                    time.sleep(10)
                    while True:
                        self.log(f"{yellow}Trying to click...")
                        if hit_available > 50:
                            click = 50000
                            try:
                                submit_click = self.submit_click(
                                    auth_data=auth_data,
                                    click=click,
                                    proxy_info=proxy_info,
                                ).json()
                                success_click = submit_click["data"]["amount"]
                                self.log(
                                    f"{green}Click success: {white}{success_click}"
                                )
                                time.sleep(10)
                                try:
                                    user_info = self.user_info(
                                        auth_data=auth_data, proxy_info=proxy_info
                                    ).json()
                                    hit_available = user_info["data"]["availableAmount"]
                                    balance = user_info["data"]["goldAmount"]
                                    self.log(f"{green}New balance: {white}{balance:,}")
                                except Exception as e:
                                    self.log(f"{red}Get balance error!!!")
                                time.sleep(10)
                            except Exception as e:
                                self.log(f"{red}Click error!!!")
                        else:
                            self.log(
                                f"{white}Number of available clicks is less than {red}50{white}. Recovery mode: {green}ON{white}"
                            )
                            break
                    wait_time = 60 * 60
                except Exception as e:
                    wait_time = 5 * 60
                    self.log(
                        f"{red}Get user info error, re-try after {int(wait_time/60)} minutes"
                    )

            print()
            self.log(f"{yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        dog = DejenDog()
        dog.main()
    except KeyboardInterrupt:
        sys.exit()
