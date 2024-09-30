import requests
import time

daily_url = "https://api-master.piggybasket.io/daily-bonus/claim"
play_game_url = "https://api-master.piggybasket.io/shot"
tasks_url = "https://api-master.piggybasket.io/missions"
clear_task_url = "https://api-master.piggybasket.io/missions/check"
upgrade_url = "https://api-master.piggybasket.io/upgrades?type=equipment"
buy_upgrade_url = "https://api-master.piggybasket.io/upgrades/"

def timer(hours):
    total_seconds = hours * 3600  # Convert hours to seconds
    while total_seconds > 0:
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Cooldown: {hours:02}:{minutes:02}:{seconds:02}", end='\r')  # Print countdown
        time.sleep(1)  # Wait for 1 second
        total_seconds -= 1
    print("Cooldown complete!")

def claim_daily_bonus(query):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Host": "api-master.piggybasket.io",
        "Origin": "https://app-master.piggybasket.io",
        "Referer": "https://app-master.piggybasket.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Telegram-Data": query,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    response = requests.post(daily_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["ok"]:
            user_info = data["result"]["user"]
            profile = {
                "telegramId": user_info["telegramId"],
                "username": user_info["username"],
                "coins": user_info["coins"]
            }
            print("Profile Information:")
            print(f"Telegram ID: {profile['telegramId']}")
            print(f"Username: {profile['username']}")
            print(f"Coins: {profile['coins']}")
        else:
            print("Failed to claim bonus.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def play_game(query):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "api-master.piggybasket.io",
        "Origin": "https://app-master.piggybasket.io",
        "Referer": "https://app-master.piggybasket.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Telegram-Data": query,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    payload = {"goal": True}

    response = requests.post(play_game_url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if data["ok"]:
            user_info = data["result"]
            print("Game Played Successfully!")
            print(f"Telegram ID: {user_info['telegramId']}")
            print(f"Username: {user_info['username']}")
            print(f"Coins: {user_info['coins']}")
            print(f"Total Goals: {user_info['totalGoals']}")
            print(f"Total Throws: {user_info['totalThrows']}")
            print(f"Streak: {user_info['streak']}")
        else:
            print("Failed to play the game.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def fetch_tasks(query):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Host": "api-master.piggybasket.io",
        "Origin": "https://app-master.piggybasket.io",
        "Referer": "https://app-master.piggybasket.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Telegram-Data": query,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    response = requests.get(tasks_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["ok"]:
            tasks = data["result"]
            print("Fetched Tasks:")
            return tasks  # Return the list of tasks
        else:
            print("Failed to fetch tasks.")
            return []
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

def clear_task(query, task_name):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "api-master.piggybasket.io",
        "Origin": "https://app-master.piggybasket.io",
        "Referer": "https://app-master.piggybasket.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Telegram-Data": query,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    payload = {"name": task_name}

    response = requests.post(clear_task_url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if data["ok"]:
            user_info = data["result"]["user"]
            completed = data["result"]["completed"]
            print("Task Completed Successfully!")
            print(f"Completed: {completed}")
            print(f"Username: {user_info['username']}")
            print(f"Coins: {user_info['coins']}")
        else:
            print("Failed to clear task.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def auto_upgrade(query):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Host": "api-master.piggybasket.io",
        "Origin": "https://app-master.piggybasket.io",
        "Referer": "https://app-master.piggybasket.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Telegram-Data": query,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    response = requests.get(upgrade_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["ok"]:
            upgrades = data["result"]
            for upgrade in upgrades:
                if upgrade["requires"] is None:  # Check if no requirements
                    # Attempt to purchase the upgrade
                    purchase_url = buy_upgrade_url + upgrade["name"]
                    purchase_response = requests.post(purchase_url, headers=headers)

                    if purchase_response.status_code == 200:
                        purchase_data = purchase_response.json()
                        if purchase_data["ok"]:
                            print(f"Purchased Upgrade: {upgrade['name']} (Level: {upgrade['level']})")
                        else:
                            print(f"Failed to purchase upgrade: {upgrade['name']}")
                    else:
                        print(f"Error purchasing upgrade: {purchase_response.status_code} - {purchase_response.text}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    while True:  # Infinite loop for continuous processing
        # Read all query data from query.txt
        with open('query.txt', 'r') as file:
            query_data_list = [line.strip() for line in file.readlines() if line.strip()]  # Read and strip lines

        for query_data in query_data_list:
            claim_daily_bonus(query_data)
            play_game(query_data)
            tasks = fetch_tasks(query_data)

            if tasks:
                task_to_clear = tasks[0]['name']  # Get the name of the first task
                clear_task(query_data, task_to_clear)  # Clear the task

            auto_upgrade(query_data)  # Attempt to auto-upgrade

        timer(24)  # Start a cooldown for 24 hours

if __name__ == "__main__":
    main()

