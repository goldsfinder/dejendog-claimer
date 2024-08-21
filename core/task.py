import requests

from smart_airdrop_claimer import base
from core.headers import headers


def check_in(token, proxies=None):
    url = "https://api.djdog.io/check/in/user/list"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        check_in_list = data["data"]
        return check_in_list
    except:
        return None


def do_check_in(token, check_in_id, proxies=None):
    url = f"https://api.djdog.io/check/in?id={check_in_id}"

    try:
        response = requests.post(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        status = data["data"]
        return status
    except:
        return None


def process_check_in(token, proxies=None):
    check_in_list = check_in(token=token, proxies=proxies)
    if check_in_list:
        for task in check_in_list:
            task_id = task["id"]
            task_reward = task["rewardAmount"]
            task_status = task["finished"]
            if task_status:
                base.log(
                    f"{base.white}Auto Check-in: {base.green}Completed | ID: {task_id}"
                )
            else:
                status = do_check_in(token=token, check_in_id=task_id, proxies=proxies)
                if status:
                    base.log(
                        f"{base.white}Auto Check-in: {base.green}Success | ID: {task_id} - Reward: {task_reward:,}"
                    )
                else:
                    base.log(
                        f"{base.white}Auto Check-in: {base.red}Fail | ID: {task_id}"
                    )
    else:
        base.log(f"{base.white}Auto Check-in: {base.red}No check-in task available")


def walk_find(token, proxies=None):
    url = "https://api.djdog.io/mission/walkFinds"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        task_list = data["data"]["missionRows"]
        return task_list
    except:
        return None


def partner(token, proxies=None):
    url = "https://api.djdog.io/mission/partners"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        task_list = data["data"]["missionRows"]
        return task_list
    except:
        return None


def group(token, proxies=None):
    url = "https://api.djdog.io/mission/group"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        group_tasks = data["data"]
        return group_tasks
    except:
        return None


def do_task(token, task_id, proxies=None):
    url = f"https://api.djdog.io/mission/finish?id={task_id}"

    try:
        response = requests.post(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        status = data["data"]
        return status
    except:
        return None


def process_do_task(token, proxies=None):
    # Walk find
    walk_find_tasks = walk_find(token=token, proxies=proxies)
    if walk_find_tasks:
        for task in walk_find_tasks:
            task_id = task["taskId"]
            task_reward = task["reward"]
            task_status = task["finished"]
            if task_status:
                base.log(
                    f"{base.white}Auto Do Task: {base.green}Completed | ID: {task_id}"
                )
            else:
                status = do_task(token=token, task_id=task_id, proxies=proxies)
                if status:
                    base.log(
                        f"{base.white}Auto Do Task: {base.green}Success | ID: {task_id} - Reward: {task_reward}"
                    )
                else:
                    base.log(
                        f"{base.white}Auto Do Task: {base.red}Fail | ID: {task_id}"
                    )
    else:
        base.log(f"{base.white}Auto Do Task: {base.red}No walk find task available")

    # Partner
    partner_tasks = partner(token=token, proxies=proxies)
    if partner_tasks:
        for task in partner_tasks:
            task_id = task["taskId"]
            task_reward = task["reward"]
            task_status = task["finished"]
            if task_status:
                base.log(
                    f"{base.white}Auto Do Task: {base.green}Completed | ID: {task_id}"
                )
            else:
                status = do_task(token=token, task_id=task_id, proxies=proxies)
                if status:
                    base.log(
                        f"{base.white}Auto Do Task: {base.green}Success | ID: {task_id} - Reward: {task_reward}"
                    )
                else:
                    base.log(
                        f"{base.white}Auto Do Task: {base.red}Fail | ID: {task_id}"
                    )
    else:
        base.log(f"{base.white}Auto Do Task: {base.red}No partner task available")

    # Group
    group_tasks = group(token=token, proxies=proxies)
    if group_tasks:
        for group_task in group_tasks:
            tasks = group_task["missionRows"]
            for task in tasks:
                task_id = task["taskId"]
                task_reward = task["reward"]
                task_status = task["finished"]
                if task_status:
                    base.log(
                        f"{base.white}Auto Do Task: {base.green}Completed | ID: {task_id}"
                    )
                else:
                    status = do_task(token=token, task_id=task_id, proxies=proxies)
                    if status:
                        base.log(
                            f"{base.white}Auto Do Task: {base.green}Success | ID: {task_id} - Reward: {task_reward}"
                        )
                    else:
                        base.log(
                            f"{base.white}Auto Do Task: {base.red}Fail | ID: {task_id}"
                        )
    else:
        base.log(f"{base.white}Auto Do Task: {base.red}No group task available")
