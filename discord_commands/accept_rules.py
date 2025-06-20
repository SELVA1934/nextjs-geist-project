import requests

API_BASE = "https://discord.com/api/v9"

def accept_rules(token, guild_id):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    # Placeholder implementation: React to rules message or send acceptance
    # For demonstration, we print a message
    print(f"\033[92mAccepted rules for guild {guild_id} with token [{token[:6]}...]. (mock implementation)\033[0m")

def run_with_token(token):
    guild_id = input(f"\033[95mEnter guild ID to accept rules for token [{token[:6]}...]: \033[0m")
    accept_rules(token, guild_id)
    choice = input("\033[95m[ 0 ] Back: \033[0m").strip()
    if choice == '0':
        return

def run_all_tokens():
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f if line.strip()]
    guild_id = input("\033[95mEnter guild ID to accept rules for all tokens: \033[0m")
    for token in tokens:
        print(f"Accepting rules for guild {guild_id} with token [{token[:6]}...]")
        accept_rules(token, guild_id)

if __name__ == "__main__":
    run_all_tokens()
