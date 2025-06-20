import requests

API_BASE = "https://discord.com/api/v9"

def bypass_onboarding(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    # Placeholder implementation: send a request to bypass onboarding
    # This is a mock implementation
    print(f"\033[92mBypassed onboarding for token [{token[:6]}...] (mock implementation).\033[0m")

def run_with_token(token):
    bypass_onboarding(token)
    choice = input("\033[95m[ 0 ] Back: \033[0m").strip()
    if choice == '0':
        return

def run_all_tokens():
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f if line.strip()]
    for token in tokens:
        print(f"Bypassing onboarding for token [{token[:6]}...]")
        bypass_onboarding(token)

if __name__ == "__main__":
    run_all_tokens()
