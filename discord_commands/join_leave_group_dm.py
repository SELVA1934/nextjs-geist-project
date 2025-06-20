import requests

API_BASE = "https://discord.com/api/v9"

def join_group_dm(token, invite_code):
    headers = {
        "Authorization": token
    }
    r = requests.post(f"{API_BASE}/invites/{invite_code}", headers=headers)
    if r.status_code == 200:
        print("Joined group DM successfully.")
    else:
        print(f"Failed to join group DM: {r.status_code} - {r.text}")

def leave_group_dm(token, channel_id):
    headers = {
        "Authorization": token
    }
    r = requests.delete(f"{API_BASE}/channels/{channel_id}", headers=headers)
    if r.status_code == 204:
        print("Left group DM successfully.")
    else:
        print(f"Failed to leave group DM: {r.status_code} - {r.text}")

def load_token():
    with open("token.txt", "r") as f:
        return f.read().strip()

def run_with_token(token):
    action = input(f"\033[95mEnter action (join/leave) for token [{token[:6]}...]: \033[0m").lower()
    if action == "join":
        invite_code = input("\033[95mEnter group DM invite code: \033[0m")
        join_group_dm(token, invite_code)
    elif action == "leave":
        channel_id = input("\033[95mEnter group DM channel ID to leave: \033[0m")
        leave_group_dm(token, channel_id)
    else:
        print("\033[93mInvalid action.\033[0m")
    choice = input("\033[95m[ 0 ] Back: \033[0m").strip()
    if choice == '0':
        return

def run_all_tokens():
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f if line.strip()]
    action = input("\033[95mEnter action (join/leave) for all tokens: \033[0m").lower()
    if action == "join":
        invite_code = input("\033[95mEnter group DM invite code for all tokens: \033[0m")
        for token in tokens:
            print(f"Joining group DM for token [{token[:6]}...]")
            join_group_dm(token, invite_code)
    elif action == "leave":
        channel_id = input("\033[95mEnter group DM channel ID to leave for all tokens: \033[0m")
        for token in tokens:
            print(f"Leaving group DM for token [{token[:6]}...]")
            leave_group_dm(token, channel_id)
    else:
        print("\033[93mInvalid action.\033[0m")

if __name__ == "__main__":
    run_all_tokens()
