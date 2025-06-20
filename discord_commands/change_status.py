import requests

API_BASE = "https://discord.com/api/v9"

def change_status(token, status):
    """
    Change Discord user status.
    Note: Discord user status is set via gateway (websocket), not REST API.
    This function is a placeholder to show intent.
    """
    print(f"[{token[:6]}...] Changing status via REST API is not supported. This requires a websocket connection.")
    # Implementation would require a websocket client to connect to Discord gateway.
    pass

def run_with_token(token):
    status = input(f"\033[95mEnter status (online, idle, dnd, invisible) for token [{token[:6]}...]: \033[0m")
    change_status(token, status)
    choice = input("\033[95m[ 0 ] Back: \033[0m").strip()
    if choice == '0':
        return

def run_all_tokens():
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f if line.strip()]
    status = input("\033[95mEnter status (online, idle, dnd, invisible) for all tokens: \033[0m")
    for token in tokens:
        print(f"Changing status for token [{token[:6]}...]")
        change_status(token, status)

if __name__ == "__main__":
    run_all_tokens()

def load_token():
    with open("token.txt", "r") as f:
        return f.read().strip()

if __name__ == "__main__":
    token = load_token()
    status = input("Enter status (online, idle, dnd, invisible): ")
    change_status(token, status)
