import sys

sys.dont_write_bytecode = True

from smart_airdrop_claimer import base
from core.token import get_token
from core.info import get_info
from core.task import process_check_in, process_do_task
from core.claim import process_claim
from core.upgrade import process_buy_box, process_buy_boost

import time
import json


class DejenDog:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data-proxy.json")
        self.config_file = base.file_path(file_name="config.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        self.banner = base.create_banner(game_name="DejenDog")

        # Get config
        self.auto_check_in = base.get_config(
            config_file=self.config_file, config_name="auto-check-in"
        )

        self.auto_do_task = base.get_config(
            config_file=self.config_file, config_name="auto-do-task"
        )

        self.auto_claim = base.get_config(
            config_file=self.config_file, config_name="auto-claim"
        )

        self.auto_buy_box = base.get_config(
            config_file=self.config_file, config_name="auto-buy-box"
        )

        self.auto_buy_boost = base.get_config(
            config_file=self.config_file, config_name="auto-buy-boost"
        )

    def main(self):
        while True:
            base.clear_terminal()
            print(self.banner)
            accounts = json.load(open(self.data_file, "r"))["accounts"]
            num_acc = len(accounts)
            base.log(self.line)
            base.log(f"{base.green}Numer of accounts: {base.white}{num_acc}")

            for no, account in enumerate(accounts):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")
                data = account["acc_info"]
                proxy_info = account["proxy_info"]
                parsed_proxy_info = base.parse_proxy_info(proxy_info)
                if parsed_proxy_info is None:
                    break

                actual_ip = base.check_ip(proxy_info=proxy_info)

                proxies = base.format_proxy(proxy_info=proxy_info)

                try:
                    token = get_token(data=data, proxies=proxies)

                    if token:

                        get_info(token=token, proxies=proxies)

                        # Check in
                        if self.auto_check_in:
                            base.log(f"{base.yellow}Auto Check-in: {base.green}ON")
                            process_check_in(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Check-in: {base.red}OFF")

                        # Do task
                        if self.auto_do_task:
                            base.log(f"{base.yellow}Auto Do Task: {base.green}ON")
                            process_do_task(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Do Task: {base.red}OFF")

                        # Claim
                        if self.auto_claim:
                            base.log(f"{base.yellow}Auto Claim: {base.green}ON")
                            process_claim(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Claim: {base.red}OFF")

                        # Buy box
                        if self.auto_buy_box:
                            base.log(f"{base.yellow}Auto Buy Box: {base.green}ON")
                            process_buy_box(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Buy Box: {base.red}OFF")

                        # Buy boost
                        if self.auto_buy_boost:
                            base.log(f"{base.yellow}Auto Buy Boost: {base.green}ON")
                            process_buy_boost(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Buy Boost: {base.red}OFF")

                        get_info(token=token, proxies=proxies)

                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = 60 * 60
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        dog = DejenDog()
        dog.main()
    except KeyboardInterrupt:
        sys.exit()
