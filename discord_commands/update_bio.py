import requests

API_BASE = "https://discord.com/api/v9"

def update_bio(token, bio):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "bio": bio
    }
    response = requests.patch(f"{API_BASE}/users/@me/profile", headers=headers, json=payload)
    if response.status_code == 200:
        print(f"[{token[:6]}...] Bio updated successfully.")
    else:
        print(f"[{token[:6]}...] Failed to update bio: {response.status_code} - {response.text}")

def run_with_token(token):
    bio = input(f"\033[95mEnter new bio for token [{token[:6]}...]: \033[0m")
    update_bio(token, bio)
    choice = input("\033[95m[ 0 ] Back: \033[0m").strip()
    if choice == '0':
        return

def run_all_tokens():
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f if line.strip()]
    bio = input("\033[95mEnter new bio for all tokens: \033[0m")
    for token in tokens:
        print(f"Updating bio for token [{token[:6]}...]")
        update_bio(token, bio)

if __name__ == "__main__":
    run_all_tokens()

def load_token():
    with open("token.txt", "r") as f:
        return f.read().strip()

if __name__ == "__main__":
    token = load_token()
    bio = input("Enter new bio: ")
    update_bio(token, bio)
