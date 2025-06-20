def boost_server(token, guild_id, amount):
    # Mock implementation of boosting a server multiple times
    print(f"\033[92mBoosted server {guild_id} with token [{token[:6]}...] {amount} times (mock implementation).\033[0m")

def run_with_token(token):
    guild_id = input(f"\033[95mEnter guild ID to boost for token [{token[:6]}...]: \033[0m")
    amount = input("\033[95mEnter amount of boosts: \033[0m")
    try:
        amount = int(amount)
    except:
        amount = 1
    boost_server(token, guild_id, amount)
    choice = input("\033[95m[ 0 ] Back: \033[0m").strip()
    if choice == '0':
        return

def run_all_tokens():
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f if line.strip()]
    guild_id = input("\033[95mEnter guild ID to boost for all tokens: \033[0m")
    amount = input("\033[95mEnter amount of boosts for all tokens: \033[0m")
    try:
        amount = int(amount)
    except:
        amount = 1
    for token in tokens:
        print(f"Boosting server for token [{token[:6]}...] {amount} times")
        boost_server(token, guild_id, amount)

if __name__ == "__main__":
    run_all_tokens()
